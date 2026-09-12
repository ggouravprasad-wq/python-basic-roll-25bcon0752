def fibonacci_series(n):
    """Generates the Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the first two terms
    series = [0, 1]
    
    # Generate the remaining terms by adding the last two numbers
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
        
    return series

# Example usage: Generate the first 10 terms
terms = 10
print(f"Fibonacci series ({terms} terms): {fibonacci_series(terms)}")
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
