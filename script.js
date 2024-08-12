document.getElementById('uploadForm').addEventListener('submit', function(event) {
    const xrayInput = document.getElementById('xray');
    if (!xrayInput.value) {
        event.preventDefault();
        alert('Please select an X-ray image.');
    }
});