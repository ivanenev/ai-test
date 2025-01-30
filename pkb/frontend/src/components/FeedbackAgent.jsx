import { useState, useEffect } from 'react';
import axios from 'axios';

const FeedbackAgent = ({ documentId }) => {
    const [stats, setStats] = useState(null);
    
    useEffect(() => {
        const fetchStats = async () => {
            try {
                const response = await axios.get(`/api/documents/${documentId}/stats`);
                setStats(response.data);
            } catch (error) {
                console.error('Error fetching document stats:', error);
            }
        };
        
        fetchStats();
    }, [documentId]);
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
            {stats && (
                <div className="mb-4 p-3 bg-white rounded-lg shadow-sm">
                    <h4 className="font-medium mb-2">Document Statistics</h4>
                    <div className="grid grid-cols-2 gap-2 text-sm">
                        <div>Average Rating: {stats.feedback_stats.average_rating}</div>
                        <div>Total Feedbacks: {stats.feedback_stats.total_feedbacks}</div>
                        <div>Positive Feedbacks: {stats.feedback_stats.positive_feedbacks}</div>
                        <div>Negative Feedbacks: {stats.feedback_stats.negative_feedbacks}</div>
                    </div>
                    {stats.feedback_stats.recent_comments.length > 0 && (
                        <div className="mt-3">
                            <h5 className="font-medium mb-1">Recent Comments</h5>
                            <ul className="space-y-1">
                                {stats.feedback_stats.recent_comments.map((comment, i) => (
                                    <li key={i} className="text-xs text-gray-600">"{comment}"</li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            )}
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
