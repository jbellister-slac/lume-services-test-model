import copy
from typing import Dict
from lume_model.models import BaseModel
from lume_model.variables import InputVariable, OutputVariable

from my_model import INPUT_VARIABLES, OUTPUT_VARIABLES



class MyModel(BaseModel):
    input_variables = copy.deepcopy(INPUT_VARIABLES)
    output_variables = copy.deepcopy(OUTPUT_VARIABLES)

    def __init__(self, **settings_kwargs):
        """Initialize the model. If additional settings are required, they can be 
        passed and handled here. For models that are wrapping model loads
        from other frameworks, this can be used for loading weights, referencing
        data files, etc.
        
        """
        super().__init__()

        # handle settings if any
        # if settings_kwargs is not None:
        # ...

    def evaluate(
        self, input_variables: Dict[str, InputVariable]
    ) -> Dict[str, OutputVariable]:
        """The evaluate method accepts input variables, performs the model execution,
        then returns a dictionary mapping variable name to output variable.

        Args:
            input_variables (Dict[str, InputVariable]): Dictionary of LUME-model input
                variables with values assigned.

        Returns:
            Dict[str, OutputVariable]: Dictionary of LUME-model output variables with
                values assigned.

        """

        ...

        return self.output_variables
