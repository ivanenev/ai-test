import { useState } from 'react';
import axios from 'axios';

const FeedbackAgent = ({ documentId }) => {
    const [feedback, setFeedback] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [message, setMessage] = useState('');
    const [rating, setRating] = useState(0);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        
        try {
            await axios.post('/api/feedback', {
                documentId,
                feedback,
                rating
            });
            setMessage('Thank you for your feedback!');
            setFeedback('');
            setRating(0);
        } catch (error) {
            setMessage('Failed to submit feedback. Please try again.');
            console.error('Feedback submission error:', error);
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <div className="mt-6 p-4 bg-gray-50 rounded-lg">
            <h3 className="text-lg font-semibold mb-3">Provide Feedback</h3>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div className="flex items-center space-x-2">
                    {[1, 2, 3, 4, 5].map((star) => (
                        <button
                            type="button"
                            key={star}
                            onClick={() => setRating(star)}
                            className={`text-2xl ${
                                star <= rating ? 'text-yellow-400' : 'text-gray-300'
                            } hover:text-yellow-500`}
                        >
                            ★
                        </button>
                    ))}
                </div>
                <textarea
                    className="w-full p-2 border rounded focus:ring-2 focus:ring-blue-500"
                    rows="3"
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                    placeholder="Your feedback..."
                    required
                />
                <button
                    type="submit"
                    className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
                    disabled={isSubmitting}
                >
                    {isSubmitting ? 'Submitting...' : 'Submit Feedback'}
                </button>
                {message && <p className="mt-2 text-sm text-gray-600">{message}</p>}
            </form>
        </div>
    );
};

export default FeedbackAgent;
