![](image.png)

# Personal Portfolio Project

A dynamic personal portfolio website built with Django, featuring smooth animations, responsive design, and interactive content sections. The site includes a blog system, skill showcase, and seamless content management.

## Features

### 1. Dynamic Content Sections
- **Infinite Scroll Skills Section**: Seamless horizontal scrolling with auto-generated duplicates
- **Interactive About Section**: Animated content reveal on scroll
- **Responsive Design**: Optimized for all device sizes
- **Blog System**: Dynamic article generation and management
- **Live Search**: Real-time article filtering

### 2. Technical Features
- **Typing Animation**: Custom text typing effect on homepage
- **Intersection Observer**: Scroll-based animations
- **Dynamic Article Generation**: Auto-generated article pages from database content
- **Media Management**: Integrated image handling for articles and portfolio content

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Font Awesome
- Google Fonts

### Backend
- Django 4.2
- MySQL/MariaDB
- Python 3.x

## Project Structure
```
PortfolioRoot/
├── Portfolio/                 # Main portfolio app
│   ├── templates/
│   │   └── home.html        # Main portfolio template
│   └── views.py
├── article/                   # Blog system app
│   ├── templates/
│   │   ├── articles.html
│   │   └── generated_articles/
│   ├── models.py
│   └── views.py
├── static/                    # Static files
│   ├── css/
│   │   └── home.css
│   └── js/
│       ├── home.js
│       └── live_search.js
├── templates/                 # Base templates
│   └── base.html
└── media/                    # User-uploaded content
```

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Configuration
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'articles',
        'USER': 'root',
        'PASSWORD': '$123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```

## Auto-Generated Content

The project features automatic HTML generation for articles:

```python
@receiver(post_save, sender=Article)
def create_article_html(sender, instance, created, **kwargs):
    if created:
        articles_dir = os.path.join(settings.BASE_DIR, 'article', 'templates', 'generated_articles')
        os.makedirs(articles_dir, exist_ok=True)
        file_path = os.path.join(articles_dir, f"{instance.title.replace(' ', '-').lower()}.html")
        # Generate HTML content
```

## Key Components

### 1. Infinite Scroll Implementation
```javascript
function autoScroll() {
    scrollAmount += scrollSpeed;
    if (scrollAmount >= container.scrollWidth / 3) {
        scrollAmount = 0;
    }
    container.scrollLeft = scrollAmount;
    requestAnimationFrame(autoScroll);
}
```

### 2. Dynamic Content Loading
```javascript
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll('.hidden');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    });
    elements.forEach((element) => observer.observe(element));
});
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Email: ameramohsen.silver@gmail.com 
- LinkedIn: [Amirah Mohsen](https://www.linkedin.com/in/amirah-mohsen-swe-258684273/)
- GitHub: [Mira-coding](https://github.com/MIRA-Coding)
