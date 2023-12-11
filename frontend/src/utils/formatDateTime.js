export const formatDateTime = (inputDate) => {
    const date = new Date(inputDate);
    const timeOptions = {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
    };
    const formattedTime = date.toLocaleTimeString('en-US', timeOptions);
    const dateOptions = {
        month: 'short',
        day: 'numeric',
        year: 'numeric'
    };
    const formattedDate = date.toLocaleDateString('en-US', dateOptions);
    const result = `${formattedTime} · ${formattedDate}`;
    return result
}
