document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const inputText = document.getElementById('floatingInput').value;

    fetch('/feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText })
    })
        .then(response => response.json())
        .then(data => {
            if (data.feedback === 'Positive') {
                document.getElementById('feedbackResult').style.color = 'green';
            }
            else {
                document.getElementById('feedbackResult').style.color = 'red';
            }
            document.getElementById('feedbackResult').innerText = 'Feedback: ' + data.feedback;
        })
        .catch(error => console.error('Error:', error));
});
