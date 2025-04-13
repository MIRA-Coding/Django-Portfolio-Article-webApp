document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector(".searchBar");
    const searchResultDiv = document.querySelector("#searchResult");
    const originalContent = searchResultDiv.innerHTML; // Save the original content
    let articles = []; // Array to store all articles

    // Function to fetch all articles and store them in the array
    async function preloadArticles() {
        try {
            const response = await fetch('/articles/fetch_all/');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            articles = data.articles; // Store articles in the array
        } catch (error) {
            console.error("Error preloading articles:", error);
        }
    }

    // Function to filter articles based on the query
    function filterArticles(query) {
        return articles.filter(article =>
            article.title.toLowerCase().includes(query.toLowerCase())
        );
    }

    // Function to render search results
    function renderResults(results) {
        searchResultDiv.innerHTML = ""; // Clear previous results
        if (results.length === 0) {
            searchResultDiv.innerHTML = "<p>No results found.</p>";
            return;
        }

        results.forEach(result => {
            const resultCard = document.createElement("div");
            resultCard.classList.add("col-lg-6");

            const cardContent = `
            <div class="row">
            <div class="col-lg-6">
                <div class="card mb-4 mt-4 d-flex flex-column"> 
                    <a href="${result.url}">
                        <img class="card-img-top" src="${result.image || 'https://via.placeholder.com/150'}" alt="${result.title}" style="aspect-ratio: 16 / 9; object-fit: cover; width: 100%;">
                    </a>
                    <div class="card-body">
                        <div class="small text-muted">${result.created_at}</div>
                        <h2 class="card-title h4">${result.title}</h2>
                        <p class="card-text">${result.content}...</p>
                        <a class="btn btn-primary mt-auto" href="${result.url}">Read more →</a>
                    </div>
                </div>
                </div>
                </div>
            `;
            resultCard.innerHTML = cardContent;
            searchResultDiv.appendChild(resultCard);
        });
    }

    // Event listener for live search
    searchInput.addEventListener("input", function () {
        const query = searchInput.value.trim();
        if (query) {
            const filteredResults = filterArticles(query); // Filter articles from the array
            renderResults(filteredResults); // Render the filtered results
        } else {
            searchResultDiv.innerHTML = originalContent; // Restore original content
        }
    });

    // Preload all articles when the page loads
    preloadArticles();
});