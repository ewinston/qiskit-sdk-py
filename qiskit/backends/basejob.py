from abc import ABC, abstractmethod

class BaseJob(ABC):
    """Class to handle asynchronous jobs"""
    
    @abstractmethod
    def __init__(self):
        """Initializes and initates the asynchronous job"""
        pass

    @abstractmethod
    def result(self):
        """
        Returns:
            qiskit.Result:
        """
        pass

    @abstractmethod
    def status(self):
        """
        Returns:
            str: 'ERROR', 'QUEUED', 'RUNNING', 'CANCELLED', or 'DONE'
        """
        pass

    @abstractmethod    
    def cancel(self):
        """
        Attempt to cancel job.
        Returns:
            bool: True if job can be cancelled, else False.
        """
        pass

    # Property attributes
    #####################
    @property
    @abstractmethod
    def running(self):
        """
        Returns:
            bool: True if job is currently running.
        """
        pass

    @property
    @abstractmethod
    def done(self):
        """
        Returns:
            bool: True if call was successfully cancelled or finished.
        """
        pass    

    @property    
    @abstractmethod
    def cancelled(self):
        """
        Returns:
            bool: True if call was successfully cancelled
        """
        pass
