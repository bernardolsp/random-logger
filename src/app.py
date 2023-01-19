import logging
from time import sleep
logging.basicConfig(level=logging.INFO)

def main():
  for i in range(1, 900):
    if i % 2 == 0:
      logging.warning("[random-logger-py]: WARN this is a warn that should be checked")
      sleep(0.6)
    if i % 3 == 0:
      logging.info("[random-logger-py]: INFO this is a info that can be ignored or checked by a flag")
      sleep(0.9)
    if i % 5 == 0:
      logging.debug("[random-logger-py]: DEBUG this is a debug that should be triggered with a flag")
      sleep(1.2)
    else:
      logging.critical("[random-logger-py]: CRITICAL: I have no clue on what is this. Please investigate.")
      sleep(3)
if __name__ == "__main__":
  main()
