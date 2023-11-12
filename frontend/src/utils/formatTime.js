export const formatRelativeTime = (dateTimeString) => {
    const now = new Date();
    const date = new Date(dateTimeString);

    const elapsedMilliseconds = now - date;
    const elapsedSeconds = Math.floor(elapsedMilliseconds / 1000);

    if (elapsedSeconds < 60) {
        return `${elapsedSeconds}s ago`;
        } else if (elapsedSeconds < 3600) {
        const minutes = Math.floor(elapsedSeconds / 60);
        return `${minutes}m ago`;
        } else if (elapsedSeconds < 86400) {
        const hours = Math.floor(elapsedSeconds / 3600);
        return `${hours}h ago`;
        } else {
        const days = Math.floor(elapsedSeconds / 86400);
        return `${days}d ago`;
        }
}