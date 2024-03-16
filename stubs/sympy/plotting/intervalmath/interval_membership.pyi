class intervalMembership:
    """Represents a boolean expression returned by the comparison of
    the interval object.

    Parameters
    ==========

    (a, b) : (bool, bool)
        The first value determines the comparison as follows:
        - True: If the comparison is True throughout the intervals.
        - False: If the comparison is False throughout the intervals.
        - None: If the comparison is True for some part of the intervals.

        The second value is determined as follows:
        - True: If both the intervals in comparison are valid.
        - False: If at least one of the intervals is False, else
        - None
    """
    def __init__(self, a, b) -> None:
        ...
    
    def __getitem__(self, i) -> Any:
        ...
    
    def __len__(self) -> Literal[2]:
        ...
    
    def __iter__(self) -> Iterator[Any]:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __and__(self, other) -> intervalMembership:
        ...
    
    def __or__(self, other) -> intervalMembership:
        ...
    
    def __invert__(self) -> intervalMembership:
        ...
    
    def __xor__(self, other) -> intervalMembership:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


