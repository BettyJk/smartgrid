
# SmartAudit

SmartAudit is a full-stack web application designed to manage and track audits and anomalies during logistics reception controls. It streamlines the process by allowing users to report issues, upload photos, and monitor performance, replacing manual tools like WhatsApp and Excel.

## Project Architecture
- **Backend:** Django REST API (`smartgrid_api`)
- **Frontend:** React (Vite, Material UI) (`smartgrid-frontend`)
- **Database:** SQLite for development, PostgreSQL for production
- **Audit Grid Source:** Dynamic forms and logic driven by `grille_audit_stellantis.json` and `.xlsx`

## Key Features
- Report anomalies and audits with photo uploads
- Secure archiving and traceability of all data
- Export data to CSV
- Multilingual support (French/Arabic)
- KPI and performance tracking
- Responsive, mobile-friendly UI

## Getting Started

### Backend Setup
1. Navigate to the backend folder:
   ```sh
   cd smartgrid
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend folder:
   ```sh
   cd smartgrid-frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```

## Deployment Guide

### Backend (Render/Railway)
1. Push your backend code to GitHub.
2. Create a new project on Render or Railway and link your repository.
3. Set environment variables as needed (see `.env.example`).
4. Add a PostgreSQL database and update your `DATABASE_URL`.
5. Deploy and run migrations:
   ```sh
   python manage.py migrate
   ```
6. Upload `grille_audit_stellantis.json` or `.xlsx` to the backend root if required.

### Frontend (Vercel/Netlify)
1. Push your frontend code to GitHub.
2. Create a new project on Vercel or Netlify and link your repository.
3. Set `VITE_API_URL` to your backend API endpoint.
4. Deploy.

## Environment Variables
- Backend: See `.env.example` for required variables.
- Frontend: Set `VITE_API_URL` to your backend API URL.

## Demo URLs
- Frontend: https://smartgrid.vercel.app
- Backend: https://smartgrid-api.up.railway.app

## License
MIT
