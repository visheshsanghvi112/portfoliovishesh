// Your Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "my-portfolio-4ca04.firebaseapp.com",
    projectId: "my-portfolio-4ca04",
    databaseURL: "https://my-portfolio-4ca04.firebaseio.com", // Add this line for Realtime Database
    storageBucket: "my-portfolio-4ca04.appspot.com",
    messagingSenderId: "935514297387",
    appId: "1:935514297387:web:fa7bef435d03188e6d466e"
};

// Function to handle form submission
export async function handleFormSubmission(name, email, subject, message) {
    try {
        // Construct request body
        const formData = {
            name: name,
            email: email,
            subject: subject,
            message: message
        };

        // Send POST request to Firebase Realtime Database
        const response = await fetch(`${firebaseConfig.databaseURL}/contacts.json`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        // Check if request was successful
        if (response.ok) {
            return "Message sent successfully!";
        } else {
            throw new Error("Failed to send message.");
        }
    } catch (error) {
        console.error("Error sending message: ", error);
        return "Error sending message. Please try again later.";
    }
}
