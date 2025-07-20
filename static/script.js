function toggleEdit(todoId) {
    const viewElement = document.getElementById('view-' + todoId);
    const editForm = document.getElementById('edit-form-' + todoId);
    const editInput = editForm.querySelector('input[type="text"]');

    if (editForm.style.display === 'none') {
        viewElement.style.display = 'none';
        editForm.style.display = 'block';
        editInput.focus();
        editInput.select();
    } else {
        viewElement.style.display = 'flex';
        editForm.style.display = 'none';
    }
}

function handleEditSubmit(todoId) {
    const editForm = document.getElementById('edit-form-' + todoId);
    const editInput = editForm.querySelector('input[type="text"]');
    const originalValue = editInput.getAttribute('data-original-value');
    const currentValue = editInput.value;

    if (originalValue.trim() !== currentValue.trim()) {
        editForm.submit();
    } else {
        toggleEdit(todoId);
    }
}