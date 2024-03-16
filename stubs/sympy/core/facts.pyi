from typing import Iterator

r"""This is rule-based deduction system for SymPy

The whole thing is split into two parts

 - rules compilation and preparation of tables
 - runtime inference

For rule-based inference engines, the classical work is RETE algorithm [1],
[2] Although we are not implementing it in full (or even significantly)
it's still worth a read to understand the underlying ideas.

In short, every rule in a system of rules is one of two forms:

 - atom                     -> ...      (alpha rule)
 - And(atom1, atom2, ...)   -> ...      (beta rule)


The major complexity is in efficient beta-rules processing and usually for an
expert system a lot of effort goes into code that operates on beta-rules.


Here we take minimalistic approach to get something usable first.

 - (preparation)    of alpha- and beta- networks, everything except
 - (runtime)        FactRules.deduce_all_facts

             _____________________________________
            ( Kirr: I've never thought that doing )
            ( logic stuff is that difficult...    )
             -------------------------------------
                    o   ^__^
                     o  (oo)\_______
                        (__)\       )\/\
                            ||----w |
                            ||     ||


Some references on the topic
----------------------------

[1] https://en.wikipedia.org/wiki/Rete_algorithm
[2] http://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-113.pdf

https://en.wikipedia.org/wiki/Propositional_formula
https://en.wikipedia.org/wiki/Inference_rule
https://en.wikipedia.org/wiki/List_of_rules_of_inference
"""
def transitive_closure(implications) -> set[Any]:
    """
    Computes the transitive closure of a list of implications

    Uses Warshall's algorithm, as described at
    http://www.cs.hope.edu/~cusack/Notes/Notes/DiscreteMath/Warshall.pdf.
    """
    ...

def deduce_alpha_implications(implications) -> defaultdict[Any, set[Any]]:
    """deduce all implications

       Description by example
       ----------------------

       given set of logic rules:

         a -> b
         b -> c

       we deduce all possible rules:

         a -> b, c
         b -> c


       implications: [] of (a,b)
       return:       {} of a -> set([b, c, ...])
    """
    ...

def apply_beta_to_alpha_route(alpha_implications, beta_rules) -> dict[Any, Any]:
    """apply additional beta-rules (And conditions) to already-built
    alpha implication tables

       TODO: write about

       - static extension of alpha-chains
       - attaching refs to beta-nodes to alpha chains


       e.g.

       alpha_implications:

       a  ->  [b, !c, d]
       b  ->  [d]
       ...


       beta_rules:

       &(b,d) -> e


       then we'll extend a's rule to the following

       a  ->  [b, !c, d, e]
    """
    ...

def rules_2prereq(rules) -> defaultdict[Any, set[Any]]:
    """build prerequisites table from rules

       Description by example
       ----------------------

       given set of logic rules:

         a -> b, c
         b -> c

       we build prerequisites (from what points something can be deduced):

         b <- a
         c <- a, b

       rules:   {} of a -> [b, c, ...]
       return:  {} of c <- [a, b, ...]

       Note however, that this prerequisites may be *not* enough to prove a
       fact. An example is 'a -> b' rule, where prereq(a) is b, and prereq(b)
       is a. That's because a=T -> b=T, and b=F -> a=F, but a=F -> b=?
    """
    ...

class TautologyDetected(Exception):
    """(internal) Prover uses it for reporting detected tautology"""
    ...


class Prover:
    """ai - prover of logic rules

       given a set of initial rules, Prover tries to prove all possible rules
       which follow from given premises.

       As a result proved_rules are always either in one of two forms: alpha or
       beta:

       Alpha rules
       -----------

       This are rules of the form::

         a -> b & c & d & ...


       Beta rules
       ----------

       This are rules of the form::

         &(a,b,...) -> c & d & ...


       i.e. beta rules are join conditions that say that something follows when
       *several* facts are true at the same time.
    """
    def __init__(self) -> None:
        ...
    
    def split_alpha_beta(self) -> tuple[list[Any], list[Any]]:
        """split proved rules into alpha and beta chains"""
        ...
    
    @property
    def rules_alpha(self) -> list[Any]:
        ...
    
    @property
    def rules_beta(self) -> list[Any]:
        ...
    
    def process_rule(self, a, b) -> None:
        """process a -> b rule"""
        ...
    


class FactRules:
    """Rules that describe how to deduce facts in logic space

       When defined, these rules allow implications to quickly be determined
       for a set of facts. For this precomputed deduction tables are used.
       see `deduce_all_facts`   (forward-chaining)

       Also it is possible to gather prerequisites for a fact, which is tried
       to be proven.    (backward-chaining)


       Definition Syntax
       -----------------

       a -> b       -- a=T -> b=T  (and automatically b=F -> a=F)
       a -> !b      -- a=T -> b=F
       a == b       -- a -> b & b -> a
       a -> b & c   -- a=T -> b=T & c=T
       # TODO b | c


       Internals
       ---------

       .full_implications[k, v]: all the implications of fact k=v
       .beta_triggers[k, v]: beta rules that might be triggered when k=v
       .prereq  -- {} k <- [] of k's prerequisites

       .defined_facts -- set of defined fact names
    """
    def __init__(self, rules) -> None:
        """Compile rules into internal lookup tables"""
        ...
    
    def print_rules(self) -> Iterator[str]:
        """ Returns a generator with lines to represent the facts and rules """
        ...
    


class InconsistentAssumptions(ValueError):
    def __str__(self) -> str:
        ...
    


class FactKB(dict):
    """
    A simple propositional knowledge base relying on compiled inference rules.
    """
    def __str__(self) -> str:
        ...
    
    def __init__(self, rules) -> None:
        ...
    
    def deduce_all_facts(self, facts) -> None:
        """
        Update the KB with all the implications of a list of facts.

        Facts can be specified as a dictionary or as a list of (key, value)
        pairs.
        """
        ...
    


