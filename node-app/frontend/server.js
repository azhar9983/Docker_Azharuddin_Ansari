const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static UI files out of the public folder
app.use(express.static(path.join(__dirname, 'public')));

// Fallback route to serve the form index page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
    console.log(`Frontend UI server running at http://localhost:${PORT}`);
});
