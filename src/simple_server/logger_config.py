import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
fh = logging.FileHandler("app.log", encoding="utf-8")

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

root_logger.addHandler(ch)
root_logger.addHandler(fh)

root_logger.propagate = True
