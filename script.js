document.getElementById('generateButton').addEventListener('click', function () {
    const place = document.getElementById('place').value;
    const duration = document.getElementById('duration').value;
    const activities = document.getElementById('activities').value;
    const extra = document.getElementById('extra').value || 'None';

    if (!place || !duration || !activities) {
        alert('Please fill in all required fields.');
        return;
    }

    const itinerary = `
        Travel Itinerary Outline
        ------------------------
        Destination: ${place}
        Duration: ${duration}
        
        Suggested Activities:
        ${activities}
        
        Additional Information:
        ${extra}
    `;

    // Display the itinerary
    document.getElementById('itinerary-output').innerText = itinerary;

    // Add save button
    const saveButton = document.createElement('button');
    saveButton.innerText = 'Save Itinerary';
    saveButton.addEventListener('click', function () {
        saveItinerary(itinerary);
    });

    // Append the save button if it doesn't already exist
    const outputDiv = document.getElementById('itinerary-output');
    outputDiv.appendChild(saveButton);
});

function saveItinerary(itinerary) {
    const blob = new Blob([itinerary], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'itinerary.txt';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
