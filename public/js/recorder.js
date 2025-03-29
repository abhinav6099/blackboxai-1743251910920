// Audio recorder and analyzer
function initRecorder(config) {
    const recordBtn = document.querySelector(config.recordBtn);
    const stopBtn = document.querySelector(config.stopBtn);
    const playBtn = document.querySelector(config.playBtn);
    const analyzeBtn = document.querySelector(config.analyzeBtn);
    const waveform = config.waveform;
    
    let mediaRecorder;
    let audioChunks = [];
    let audioBlob;
    let audioUrl;
    let audioElement = new Audio();
    
    // Check for recording support
    if (!navigator.mediaDevices || !window.MediaRecorder) {
        recordBtn.disabled = true;
        recordBtn.textContent = 'Recording not supported';
        return;
    }
    
    // Setup recording
    recordBtn.addEventListener('click', async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(stream);
            audioChunks = [];
            
            mediaRecorder.ondataavailable = (e) => {
                audioChunks.push(e.data);
            };
            
            mediaRecorder.onstop = () => {
                audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                audioUrl = URL.createObjectURL(audioBlob);
                waveform.load(audioUrl);
                playBtn.disabled = false;
                analyzeBtn.disabled = false;
            };
            
            mediaRecorder.start();
            recordBtn.disabled = true;
            stopBtn.disabled = false;
            waveform.empty();
        } catch (err) {
            console.error('Recording failed:', err);
            alert('Could not start recording. Please ensure microphone access is allowed.');
        }
    });
    
    // Stop recording
    stopBtn.addEventListener('click', () => {
        mediaRecorder.stop();
        recordBtn.disabled = false;
        stopBtn.disabled = true;
        
        // Stop all tracks
        mediaRecorder.stream.getTracks().forEach(track => track.stop());
    });
    
    // Play recording
    playBtn.addEventListener('click', () => {
        if (audioUrl) {
            audioElement.src = audioUrl;
            audioElement.play();
            waveform.play();
        }
    });
    
    // Analyze recording
    analyzeBtn.addEventListener('click', () => {
        if (!audioBlob) return;
        
        // In a real app, we would send the audio to the server for analysis
        // For now, we'll mock the response
        setTimeout(() => {
            const mockResult = {
                score: Math.floor(Math.random() * 30) + 70, // Random score 70-100
                feedback: "Good effort! Pay attention to the vowel lengths in the second half."
            };
            
            if (config.onAnalysisComplete) {
                config.onAnalysisComplete(mockResult);
            }
        }, 1500);
        
        // Show loading state
        if (config.onAnalysisComplete) {
            config.onAnalysisComplete({
                score: 0,
                feedback: "Analyzing your pronunciation..."
            });
        }
    });
    
    // Connect waveform to audio element
    waveform.on('finish', () => {
        audioElement.pause();
        audioElement.currentTime = 0;
    });
}

export { initRecorder };