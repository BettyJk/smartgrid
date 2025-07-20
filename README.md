# SmartGrid

SmartGrid is a full-stack web application to digitize the logistics audit grid for Stellantis. It features a Django REST API backend and a React (Vite + MUI) frontend, with multilingual support (French/Arabic), dynamic Excel-driven forms, and production-ready deployment configs.

## Features
- Django backend with DRF, SQLite (dev), PostgreSQL (prod)
- React frontend with Material UI, i18n (French/Arabic)
- Dynamic audit grid from Excel (`grille_audit_stellantis.xlsx`)
- User authentication (email/password)
- Responsive, mobile-friendly UI
- Ready for deployment: Railway/Render (backend), Vercel (frontend)

## Local Development

### Backend
1. `cd smartgrid`
2. Create a virtual environment and activate it:
   - Windows: `python -m venv venv && .\venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

### Frontend
1. `cd smartgrid-frontend`
2. Install dependencies: `npm install`
3. Start dev server: `npm run dev`

## Deployment
- Backend: Deploy to Railway or Render (see `smartgrid_api` docs)
- Frontend: Deploy to Vercel (see `smartgrid-frontend` docs)

## Environment Variables
See `.env.example` in both backend and frontend folders for required variables.
  - Railway/Render: Set environment variables from `.env.production.example` in the dashboard.
  - Vercel: Set `VITE_API_URL` in the dashboard to your backend API URL.

## Deployment Steps

### Backend (Railway/Render)
1. Push your code to GitHub.
2. Create a new project on Railway or Render, link your repo.
3. Set environment variables from `.env.production.example`.
4. Add a PostgreSQL database (Railway/Render provides this) and update `DATABASE_URL`.
5. Deploy and run migrations:
   - Railway: Use the web shell or CI to run `python manage.py migrate`.
6. Upload `grille_audit_stellantis.xlsx` to the root of your deployed backend.

### Frontend (Vercel)
1. Push your frontend code to GitHub.
2. Create a new project on Vercel, link your repo.
3. Set `VITE_API_URL` to your backend API endpoint.
4. Deploy.

## Demo URLs
- Frontend: https://smartgrid.vercel.app
- Backend: https://smartgrid-api.up.railway.app

## License
MIT
