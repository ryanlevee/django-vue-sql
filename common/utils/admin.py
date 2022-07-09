def append_fields(fieldsets, fieldset, fields):
    """Appends new fields to a fieldset in fieldsets.

    Args:
        fieldsets (tuple): The fieldsets to append to.
            - fieldsets for editing existing objects
            - add_fieldsets for adding new objects
        fieldset (str or None): The title of the fieldset.
            None for the titleless fieldset.
        fields (tuple): The fields to append.

    Returns:
        tuple: The modified fieldsets.
    """
    for _fieldset in fieldsets:
        if _fieldset[0] == fieldset:
            _fieldset[1]['fields'] += fields
            break
    else: # Fieldset doesn't exist yet. Add new fieldset.
        fieldsets = fieldsets + (
            (fieldset, {
                'classes': ('wide',),
                'fields': fields
            }),
        )

    return fieldsets


def remove_fields(fieldsets, fieldset, fields):
    """Removes fields from fieldset in fieldsets.

    Args:
        fieldsets (tuple): The fieldsets to modify.
            - fieldsets for editing existing objects
            - add_fieldsets for adding new objects
        fieldset (str or None): The title of the fieldset from which to
            remove the field.
        fields (tuple): The fields to remove.

    Returns:
        tuple: The modified fieldsets.
    """
    for _fieldset in fieldsets:
        if _fieldset[0] == fieldset:
            field_list = list(_fieldset[1]['fields'])
            for field in fields:
                field_list.remove(field) # raises exception if field not found
            _fieldset[1]['fields'] = tuple(field_list)
            break
    else:
        raise Exception(f'No such fieldset: {fieldset}')

    return fieldsets


def move_fields(fieldsets, from_fieldset, to_fieldset, fields):
    """Moves fields from from_fieldset to to_fieldset in fieldsets.

    Args:
        fieldsets (tuple): [description]
        from_fieldset (str or None): The title of the fieldset from which to
            remove the field.
        to_fieldset (str or None): The title of the fieldset in which to
            add the field.
        fields (tuple): The fields to remove.

    Returns:
        tuple: The modified fieldsets.
    """
    remove_fields(fieldsets, from_fieldset, fields)
    append_fields(fieldsets, to_fieldset, fields)

    return fieldsets