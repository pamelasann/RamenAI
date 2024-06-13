const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const OpenAI = require("openai");
const mongoose = require('mongoose');
require('dotenv').config();

// Creación de aplicación de Express
const app = express();
const port = 3001;

// Middlewares
app.use(cors());
app.use(bodyParser.json());

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

let conversationHistory = [
    { role: "system", content: "Eres un excelente cocinero y experto en ramen. Eres bueno en descubrir e inventar nuevas formas de preparar y disfrutar ramen en casa. Das recetas sencillas e instrucciones concisas." }
];

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.log('Failed to connect to MongoDB', err));

// Define Schema and Model
const conversationSchema = new mongoose.Schema({
    userId: String, // Add userId to the schema
    role: String,
    content: String,
    timestamp: { type: Date, default: Date.now }
});

const Conversation = mongoose.model('Conversation', conversationSchema);

app.post('/api/maruchat', async (req, res) => {
    try {
        const userId = req.userId; // Extracted from middleware
        const userInput = req.body.userInput;

        if (userInput != null) conversationHistory.push({ userId, role: "user", content: userInput });

        const completion = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: conversationHistory
        });

        const chatResponse = completion.choices[0].message.content;
        conversationHistory.push({ role: "assistant", content: chatResponse });

        // Save the conversation history to MongoDB
        const conversationRecords = conversationHistory.map(message => {
            return new Conversation({
                userId,
                role: message.role,
                content: message.content,
                timestamp: message.timestamp
            });
        });
        
        await Conversation.insertMany(conversationRecords);

        res.json({ chatResponse });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});


app.get('/api/conversations', async (req, res) => {
    try {
        const userId = req.userId; // Extracted from middleware
        const conversations = await Conversation.find({ userId });
        res.json(conversations);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});