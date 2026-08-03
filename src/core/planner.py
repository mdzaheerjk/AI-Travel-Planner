from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger=get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.message=[]
        self.city=""
        self.interests=[]
        self.itineary=""

    def set_city(self,city:str):
        try:
            self.city=city
            self.message.append(HumanMessage(content=city))
            logger.info("City set Succesfully")
        except Exception as e:
            logger.error(f"error while setting city : {e}")
            raise CustomException("Failed to set city",e)

    def set_interests(self,interests_str:str):
        try:
            self.interests=[i.strip() for i in interests_str.split(",")]
            self.message.append(HumanMessage(content=interests_str))
            logger.info("Interest also set sucesfully...")
        except Exception as e:
            logger.error(f"error while setting interests :{e}")
            raise CustomException("Failed to set interest ",e)
    def create_itineary(self):
        try:
            logger.info(f"Generating itineary for {self.city} and for itineary :{self.interests}")
            itineary=generate_itineary(self.city,self.interests)
            self.interests=self.itineary
            self.message.append(AIMessage(content=self.itineary))
            logger.info("Itineary generated succesfully")
            return itineary
        except Exception as e:
            logger.error(f"error while creating itineary:{e}")
            raise CustomException("failed to create itineary",e)
