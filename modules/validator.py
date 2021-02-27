from dataclasses import dataclass


@dataclass
class Validator:

    def zip_check(self, list_to_validate) -> bool:
        is_list_ready_to_zip: bool = False

        if len(list_to_validate) > 0:
            if not any(element is None for element in list_to_validate):
                is_list_ready_to_zip = True

        return is_list_ready_to_zip
