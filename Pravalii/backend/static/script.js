let mediaRecorder;
let audioChunks = [];

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.start();

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };
}

function stopRecording() {
    mediaRecorder.stop();

    mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const file = new File([audioBlob], "voice.wav");

        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);

        document.getElementById("audioFile").files = dataTransfer.files;
        alert("Voice recorded! Click Analyze Emotion.");
    };
}
