# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_input_json.ipynb.

# %% auto 0
__all__ = ['load_statement', 'pretty_print_statement', 'get_value', 'get_actor', 'get_actor_name', 'get_verb', 'get_verb_str',
           'get_object', 'get_object_definition', 'get_object_description', 'get_stored', 'get_timestamp',
           'get_time_diff', 'is_active', 'is_voided', 'has_generated_id', 'get_client', 'get_LRS', 'get_id',
           'get_persona_id', 'get_organisation', 'get_hash', 'get_completed_fw_queues', 'get_failed_fw_log',
           'get_completed_queues', 'get_dead_forwarding_queues', 'get_pending_forwarding_queues',
           'get_processing_queues', 'get_registrations']

# %% ../nbs/00_input_json.ipynb 4
import json
from typing import Union, List
from datetime import datetime, timedelta
from pathlib import Path
from fastcore.test import *

# %% ../nbs/00_input_json.ipynb 8
def load_statement(json_file: str # Filename of the json containing the statement
                  ) -> dict: # A dictionary representing the statement structure
    """
    Load a json from file and store the information in a Python dictionary object.
    If the file does not exist, returns an empty dict and print an error message
    """
    if Path(json_file).exists():
        with open(json_file) as f:
            return json.load(f)
    else:
        print("ERROR: The specified file does not exist")
        return dict()

# %% ../nbs/00_input_json.ipynb 10
def pretty_print_statement(statement: dict, # the statement dict imported from JSON
                          indent: int=4 # indentation used when printing
                          ) -> None:
    """
    Displays the content of the statement in a human readable format
    """
    print(json.dumps(statement, indent=indent))

# %% ../nbs/00_input_json.ipynb 12
def get_value(statement: dict, # Our xAPI statement imported from JSON
              key: str # The key we are interested in
             ) -> Union[str, dict, List, None]: # The value associated to the key in the statement
    """
    Return the value associated to the specified key in the statement dictionary.
    If the key does not exist, returns None
    """
    if key in statement:
        return statement[key]
    else:
        return None

# %% ../nbs/00_input_json.ipynb 15
def get_actor(statement: dict, # Our xAPI statement imported from JSON
             ) -> dict: # dictionary containing actor information
    """
    Extract the actor information from the statement
    """
    st = get_value(statement, "statement")
    #pretty_print_statement(st["actor"], indent = 2)
    return st["actor"]

# %% ../nbs/00_input_json.ipynb 17
def get_actor_name(statement: dict, # Our xAPI statement imported from JSON
             ) -> str: # name of the actor
    """
    Quick access to the name field of the actor, as it is the most relevant information
    """
    st = get_value(statement, "statement")
    return st["actor"]["name"]

# %% ../nbs/00_input_json.ipynb 19
def get_verb(statement: dict, # Our xAPI statement imported from JSON
             ) -> dict: # dictionary containing verb information
    """
    Extract the verb information from the statement
    """
    st = get_value(statement, "statement")
    return st["verb"]

# %% ../nbs/00_input_json.ipynb 21
def get_verb_str(statement: dict, # Our xAPI statement imported from JSON
             ) -> str: # the displayed verb
    """
    Quick access to the display field of the verb, as it is the most relevant information
    """
    st = get_value(statement, "statement")
    return st["verb"]["display"]["en-US"]

# %% ../nbs/00_input_json.ipynb 23
def get_object(statement: dict, # Our xAPI statement imported from JSON
             ) -> dict: # dictionary containing object information
    """
    Extract the object information from the statement
    """
    st = get_value(statement, "statement")
    return st["object"]

# %% ../nbs/00_input_json.ipynb 25
def get_object_definition(statement: dict, # Our xAPI statement imported from JSON
             ) -> str: # the object definition
    """
    Quick access to the object definition
    """
    st = get_value(statement, "statement")
    return st["object"]["definition"]["name"]["en-US"]

# %% ../nbs/00_input_json.ipynb 27
def get_object_description(statement: dict, # Our xAPI statement imported from JSON
             ) -> str: # the object description
    """
    Quick access to the object description
    """
    st = get_value(statement, "statement")
    return st["object"]["definition"]["description"]["en-US"]

# %% ../nbs/00_input_json.ipynb 31
def get_stored(statement: dict, # Our xAPI statement imported from JSON
              ) -> datetime: # datetime object representing the time the statement was stored in the database
    """
    Extract the date and time information of when the statement was stored in the database
    """
    stored_str = get_value(statement, "stored")
    return datetime.strptime(stored_str, "%Y-%m-%dT%H:%M:%S.%f%z")

# %% ../nbs/00_input_json.ipynb 33
def get_timestamp(statement: dict, # Our xAPI statement imported from JSON
              ) -> datetime: # datetime object representing the time the statement was generated
    """
    Extract the date and time information of when the statement was created
    """
    timestamp_str = get_value(statement, "timestamp")
    return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f%z")

# %% ../nbs/00_input_json.ipynb 35
def get_time_diff(statement: dict, # Our xAPI statement imported from JSON
                 ) -> timedelta:   # Time difference between when the statement was sent and when it was stored
    """
    Compute the time difference between when a statement was sent and when it was stored in the database
    """
    ts_sent = get_timestamp(statement)
    ts_stored = get_stored(statement)
    return ts_stored - ts_sent

# %% ../nbs/00_input_json.ipynb 38
def is_active(statement: dict, # Our xAPI statement imported from JSON
              ) -> bool: # Boolean representive whether active or not
    """
    Extract the Active field from the statement
    """
    return get_value(statement, "active")

# %% ../nbs/00_input_json.ipynb 40
def is_voided(statement: dict, # Our xAPI statement imported from JSON
              ) -> bool: # Boolean representive whether statement is voided or not
    """
    Extract the Active field from the statement
    """
    return get_value(statement, "voided")

# %% ../nbs/00_input_json.ipynb 42
def has_generated_id(statement: dict, # Our xAPI statement imported from JSON
              ) -> bool: # Boolean representive whether statement has generated id
    """
    Extract the Active field from the statement
    """
    return get_value(statement, "hasGeneratedId")

# %% ../nbs/00_input_json.ipynb 45
def get_client(statement: dict, # Our xAPI statement imported from JSON
              ) -> str: # ID of the client
    """
    Extract the client field from the statement
    """
    return get_value(statement, "client")

# %% ../nbs/00_input_json.ipynb 47
def get_LRS(statement: dict, # Our xAPI statement imported from JSON
              ) -> str: # ID of the Learning Record Store
    """
    Extract the Learning Record Store ID field from the statement
    """
    return get_value(statement, "lrs_id")

# %% ../nbs/00_input_json.ipynb 49
def get_id(statement: dict, # Our xAPI statement imported from JSON
              ) -> str: # ID of the statement
    """
    Extract the ID field from the statement
    """
    return get_value(statement, "_id")

# %% ../nbs/00_input_json.ipynb 51
def get_persona_id(statement: dict, # Our xAPI statement imported from JSON
              ) -> str: # id of the persona associated to the statement
    """
    Extract the persona identifier
    """
    return get_value(statement, "personaIdentifier")

# %% ../nbs/00_input_json.ipynb 53
def get_organisation(statement: dict, # Our xAPI statement imported from JSON
              ) -> str: # id of the organization to the statement
    """
    Extract the persona identifier
    """
    return get_value(statement, "organisation")

# %% ../nbs/00_input_json.ipynb 55
def get_hash(statement: dict, # Our xAPI statement imported from JSON
              ) -> str: # hash of the statement
    """
    Extract the hash
    """
    return get_value(statement, "hash")

# %% ../nbs/00_input_json.ipynb 58
def get_completed_fw_queues(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of completed forwarding queues in the statement
    """
    Extract the List of completed forwarding queues in the statement
    """
    return get_value(statement, "completedForwardingQueue")

# %% ../nbs/00_input_json.ipynb 60
def get_failed_fw_log(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of failed forwarding log messages in the statement
    """
    Extract the List of failed forwarding log messages in the statement
    """
    return get_value(statement, "failedForwardingLog")

# %% ../nbs/00_input_json.ipynb 62
def get_completed_queues(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of completed queues in the statement
    """
    Extract the List of completed queues in the statement
    """
    return get_value(statement, "completedQueues")

# %% ../nbs/00_input_json.ipynb 64
def get_completed_queues(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of completed queues in the statement
    """
    Extract the List of completed queues in the statement
    """
    return get_value(statement, "completedQueues")

# %% ../nbs/00_input_json.ipynb 66
def get_dead_forwarding_queues(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of dead forwarding queues in the statement
    """
    Extract the List of dead forwarding queues in the statement
    """
    return get_value(statement, "deadForwardingQueue")

# %% ../nbs/00_input_json.ipynb 68
def get_pending_forwarding_queues(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of completed queues in the statement
    """
    Extract the List of pending forwarding queues in the statement
    """
    return get_value(statement, "pendingForwardingQueue")

# %% ../nbs/00_input_json.ipynb 70
def get_processing_queues(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of processing queues in the statement
    """
    Extract the List of processing queues in the statement
    """
    return get_value(statement, "processingQueues")

# %% ../nbs/00_input_json.ipynb 72
def get_registrations(statement: dict, # Our xAPI statement imported from JSON
                ) -> List: # List of registrations in the statement
    """
    Extract the List of registrations in the statement
    """
    return get_value(statement, "registrations")
