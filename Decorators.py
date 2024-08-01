import time
def timed(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    return result
  return wrapper

@timed
def my_function():
  # run some operation
  time.sleep(2)
  pass

my_function()
