/**
 *  mclib.h
 *
 *  Common library utilities.
 */


#ifndef __MCLIB_H
#define __MCLIB_H 1

/**
 *  Stringify (add quotes to) the bare word argument
 */
#define __str_quote(...) #__VA_ARGS__

/**
 *  Wrapper for __test_command allowing bare words
 */
#define TEST_CMD(...) __test_command(__str_quote(__VA_ARGS__))

/**
 * Inject the command (bare words) into the resulting ASM
 */
#define CMD(...) __asm__(__str_quote(CMD __VA_ARGS__))

/**
 * Swaps the value of the two arguments without the use of a temporary variable
 */
#define ASM_swap(a, b) __asm__("XCHG >?, >?", a, b)

#endif /* __MCLIB_H */
