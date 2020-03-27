from collections import deque
from typing import TypeVar, Final, Callable, Any, Optional, Iterable, Dict, Union, Type

__version__ = "0.0.0"

T = TypeVar('T')
R = TypeVar('R')
S = TypeVar('S')

def fn(*exprs: Any, ret: Optional[T]=None) -> Optional[T]:
    return ret

def for_each(items: Iterable[T], f: Callable[[T], None], /) -> None:
    for item in items:
        f(item)

# Inspired by `with-handlers` in Racket:
# https://docs.racket-lang.org/reference/exns.html#%28form._%28%28lib._racket%2Fprivate%2Fmore-scheme..rkt%29._with-handlers%29%29
def with_handlers(handlers: Dict[Type[Exception], Callable[[Exception], S]], f: Callable[[], T]) -> Union[S, T]:
    try:
        return f()
    except tuple(handlers.keys()) as err:
        return handlers[type(err)](err)


def catch(
        try_clause: Callable[[], T],
        except_clauses: Dict[Type[Exception], Callable[[Exception], S]],
        else_clause: Optional[Callable[[T], R]] = None,
        final_clause: Optional[Callable[[Union[T, S]], None]] = None) -> Union[R, S, T]:
    ok: bool
    ret: T = None
    handled: S = None
    try:
        ret: T = try_clause()
    except tuple(except_clauses.keys()) as err:
        ok = False
        handled: S = except_clauses[type(err)](err)
        return handled
    else:
        ok = True
        return ret if else_clause is None else else_clause(ret)
    finally:
        if final_clause is not None:
            if ok:
                final_clause(ret)
            else:
                final_clause(handled)
