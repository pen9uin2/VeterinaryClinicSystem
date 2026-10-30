from DAL.repository import OwnerRepository

class OwnerService:
    @staticmethod
    def register(first_name, last_name, phone, email):
        OwnerRepository.add_owner(first_name, last_name, phone, email)
        return True