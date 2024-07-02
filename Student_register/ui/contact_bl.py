from typing import Any, Iterator, Hashable
from utility import search
from datasource_management import save_data, load_data, save_iter_data

CONTACT_FILE_PATH = r"file/contact.txt"


def convert_listdict_to_liststr(data: list[dict]) -> Iterator[str]:
    return map(lambda item: f"{item}\n", data)


def convert_liststr_to_listdict(data: list[str]) -> Iterator[dict]:
    return map(lambda item: eval(item.strip()), data)


def _validation(contact: dict):
    function_result = {
        "SUCCESS": True,
        "ERROR_MESSAGE": {},
        "SUCCESS_MESSAGE": {},
        "RETURN_DATA": None
    }

    name = contact.get("name").strip()
    family = contact.get("family").strip()
    phone = contact.get("phone").strip()
    gender = contact.get("gender").strip()
    description = contact.get("description").strip()

    if not name:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["name"] = "name is empty!"
    elif not name.isalpha():
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["name"] = "name is not alphabetical!"

    if not family:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["family"] = "family is empty!"
    elif not family.isalpha():
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["family"] = "family is not alphabetical!"

    if not gender:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["gender"] = "gender is empty!"
    elif gender not in ("male", "female", "other"):
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["gender"] = "gender not in male, female, other!"

    if not phone:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = "The phone is empty!"
    elif not phone.isdecimal():
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = "The phone is not decimal!"
    elif len(phone) != 11:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = "The phone is not 11 digits!"

    return function_result


def create_contact(contact: dict) -> dict:
    function_result = {
        "SUCCESS": True,
        "ERROR_MESSAGE": {},
        "SUCCESS_MESSAGE": {},
        "RETURN_DATA": None
    }

    # region validation
    result = _validation(contact=contact)

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result
    # endregion

    # region ckeck unique phone
    result = get_contacts()

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    for cnt in result["RETURN_DATA"]:
        if cnt["phone"] == contact["phone"]:
            function_result["SUCCESS"] = False
            function_result["ERROR_MESSAGE"]["phone"] = f"{contact['phone']} exist"

            return function_result

    # endregion

    # region save data
    result = save_data(
        path=CONTACT_FILE_PATH,
        data=f"{contact}\n",
        mode="a"
    )

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    function_result["SUCCESS_MESSAGE"]["success"] = "Horaaa :)"
    return function_result
    # endregion


def get_contacts(*columns: str):
    function_result = {
        "SUCCESS": True,
        "ERROR_MESSAGE": {},
        "SUCCESS_MESSAGE": {},
        "RETURN_DATA": None
    }

    result = load_data(path=CONTACT_FILE_PATH)

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    contact_list = convert_liststr_to_listdict(result["RETURN_DATA"])

    if not columns:
        function_result["RETURN_DATA"] = contact_list
    else:
        function_result["RETURN_DATA"] = map(
            lambda contact: {col: contact[col] for col in columns},
            contact_list
        )

    return function_result


def remove_contact(phone: str) -> dict:
    function_result = {
        "SUCCESS": True,
        "ERROR_MESSAGE": {},
        "SUCCESS_MESSAGE": {},
        "RETURN_DATA": None
    }

    # region validation
    if not phone:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = "The phone is empty!"
    elif not phone.isdecimal():
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = "The phone is not decimal!"
    elif len(phone) != 11:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = "The phone is not 11 digits!"

    if not function_result["SUCCESS"]:
        return function_result
    # endregion

    # region ckeck unique phone
    result = get_contacts()

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    contact_list = list(result["RETURN_DATA"])

    for contact in contact_list:
        if contact["phone"] == phone:
            contact_list.remove(contact)
            break
    else:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = f"{phone} does not exist"
        return function_result
    # endregion

    # region save data
    result = save_iter_data(
        path=CONTACT_FILE_PATH,
        data=convert_listdict_to_liststr(contact_list),
        mode="w"
    )

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    function_result["SUCCESS_MESSAGE"]["success"] = "Horaaa :)"
    return function_result
    # endregion


def edit_contact(contact: dict) -> dict:
    function_result = {
        "SUCCESS": True,
        "ERROR_MESSAGE": {},
        "SUCCESS_MESSAGE": {},
        "RETURN_DATA": None
    }

    # region validation
    result = _validation(contact=contact)

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result
    # endregion

    # region ckeck unique phone
    result = get_contacts()

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    contact_list = list(result["RETURN_DATA"])

    for cnt in contact_list:
        if cnt["phone"] == contact["phone"]:
            cnt.update(contact)
            break
    else:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"]["phone"] = f"{contact['phone']} does not exist"

        return function_result
    # endregion

    # region save data
    result = save_iter_data(
        path=CONTACT_FILE_PATH,
        data=convert_listdict_to_liststr(contact_list),
        mode="w"
    )

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    function_result["SUCCESS_MESSAGE"]["success"] = "Horaaa :)"
    return function_result
    # endregion


def search_contact(key: Hashable, val: Any):
    function_result = {
        "SUCCESS": True,
        "ERROR_MESSAGE": {},
        "SUCCESS_MESSAGE": {},
        "RETURN_DATA": None
    }

    result = get_contacts()

    if not result["SUCCESS"]:
        function_result["SUCCESS"] = False
        function_result["ERROR_MESSAGE"] = result["ERROR_MESSAGE"]
        return function_result

    function_result["RETURN_DATA"] = search(
        data_list=result["RETURN_DATA"], key=key, val=val)
    return function_result
