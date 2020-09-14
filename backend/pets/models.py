from enum import Enum
from pydantic import BaseModel
from typing import List, Optional


class PetState(str, Enum):
    """[summary]
        Used to manage supported pet states.
    [description]
        Simple enumeration to link the pets state.
    """
    injured = "Injured"
    underfed = "Underfed"
    critical = "Critical"
    bad = "Bad"
    good = "Good"


class PetKind(str, Enum):
    """[summary]
        Used to manage supported pets.
    [description]
        Simple enumeration to link the kind of a pet.
    """
    dog = "Dog"
    cat = "Cat"


class PetBase(BaseModel):
    """[summary]
        Base pet abstraction model.
    [description]
        Used to abstract out basic pet fields.
    Arguments:
        BaseModel {[type]} -- [description]
    """
    kind: PetKind
    states: List[PetState]
    location: str
    picture: Optional[str] = None
    rescued: bool = False
    adopted: bool = False
    in_temp_house: bool = False
    ready_for_adoption: bool = False
    name: Optional[str] = None


class PetOnDB(PetBase):
    """[summary]
    Actual model used at DB level
    [description]
    Extends:
        PetBase
    Adds `_id` field.
    Variables:
        id_: str {[ObjectId]} -- [id at DB]
    """
    id_: str