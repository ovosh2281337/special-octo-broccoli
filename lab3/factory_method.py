class FileLogger:
    def log(self, message):
        # Условный вывод, как в примере из лекции.
        print("Logging to file:", message)


class ConsoleLogger:
    def log(self, message):
        print("Logging to console:", message)


class LoggerFactory:
    def createLogger(self):
        raise NotImplementedError

    def logMessage(self, message):
        logger = self.createLogger()
        logger.log(message)


class FileLoggerFactory(LoggerFactory):
    def createLogger(self):
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):
    def createLogger(self):
        return ConsoleLogger()
