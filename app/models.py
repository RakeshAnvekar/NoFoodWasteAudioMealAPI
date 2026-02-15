from pydantic import BaseModel, Field
from typing import List, Optional

from pydantic import BaseModel, Field
from typing import Optional, List

class FoodMetadata(BaseModel):
    location: Optional[str] = Field(
        default=None,
        description="Location of the food items"
    )

    food_items: Optional[List[str]] = Field(
        default=None,
        description="List of food items"
    )

    quantity: Optional[str] = Field(
        default=None,
        description="Quantity of the food items"
    )

    quality: Optional[str] = Field(
        default=None,
        description="Quality of the food items"
    )

    pickup_time: Optional[str] = Field(
        default=None,
        description="Pickup time for the food items"
    )
