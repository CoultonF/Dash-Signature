# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Test(Component):
    """A Test component.


    Keyword arguments:

    - id (string; optional):
        The ID used to identify this component in Dash callbacks."""

    _children_props = []
    _base_nodes = ["children"]
    _namespace = "dash_signature"
    _type = "Test"

    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ["id"]
        self._valid_wildcard_attributes = []
        self.available_properties = ["id"]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop("_explicit_args")
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Test, self).__init__(**args)