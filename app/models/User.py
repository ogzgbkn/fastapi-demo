from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Boolean
from app.models.TimestampAbstractModel import TimestampAbstractModel
from app.db.database import Base
from app.models.modelChoices import userGenderChoices, userCountryOfAsylumChoices, userNationalityChoices
from datetime import date

# The model for the cases of the end users
class User(Base, TimestampAbstractModel):
    __tablename__ = "User"

    ID = Column(BigInteger, primary_key=True, index=True)
    Name = Column(String(255), nullable=False)
    Surname = Column(String(255), nullable=False)
    DateOfBirth = Column(DateTime, nullable=False)
    PlaceOfBirth = Column(String(255), nullable=False)

    # NOTE: You can use Enum in SQLAlchemy for choices if desired
    Gender = Column(String(20), nullable=False)

    PhoneNumber = Column(String(30), nullable=False)
    EmailAddress = Column(String(255), unique=True, nullable=False, index=True)

    ProvinceOfResidence = Column(String(255), nullable=False)
    CountryOfAsylum = Column(String(255), nullable=False)
    Nationality = Column(String(255), nullable=False)

    NationalIdNumber = Column(String(255), nullable=True)
    CountryOfAsylumRegistrationNumber = Column(String(255), nullable=True)
    UnhcrIndividualId = Column(String(255), nullable=True)
    HouseholdPersonCount = Column(Integer, nullable=True)

    ReceiveMessagesFromUnhcr = Column(Boolean, default=False)
    ReceiveNotificationsFromUnhcr = Column(Boolean, default=False)
    ReceiveSurveysFromUnhcr = Column(Boolean, default=False)

    # You can optionally define a method to calculate age (not used by SQLAlchemy directly)
    def calculate_age(self):
        today = date.today()
        birth_date = self.DateOfBirth
        return (
            today.year - birth_date.year -
            ((today.month, today.day) < (birth_date.month, birth_date.day))
        )