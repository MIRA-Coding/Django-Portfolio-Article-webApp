document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector(".form-control");
    const searchResultDiv = document.querySelector("#searchResult");
    const originalContent = searchResultDiv.innerHTML; // Save the original content

    // Function to fetch and render search results
    async function fetchResults(query) {
        try {
            const response = await fetch(`/articles/search/?q=${query}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const html = await response.text(); // Get the HTML response
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");
            const newContent = doc.querySelector("#searchResult").innerHTML; // Extract the updated content
            searchResultDiv.innerHTML = newContent; // Replace the content
        } catch (error) {
            console.error("Error fetching search results: hi hi", error);
            searchResultDiv.innerHTML = "<p>An error occurred while fetching searhhhhhhhch results. Please try again later.</p>";
        }
    }

    // Event listener for live search
    searchInput.addEventListener("input", function () {
        const query = searchInput.value.trim();
        if (query) {
            fetchResults(query);
        } else {
            searchResultDiv.innerHTML = originalContent; // Restore original content
        }
    });
});