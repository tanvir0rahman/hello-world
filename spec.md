# Professional Headshot AI App - Specification

## Overview
A web application that transforms user-uploaded photos into professional headshots using AI-powered image generation. Users can select from multiple professional styles and compare the generated headshot side-by-side with their original photo.

## Core Features

### 1. Photo Upload
- Users can upload a photo from their device
- Supported formats: JPEG, PNG, WEBP
- Image size validation (max 5MB)
- Preview uploaded image before processing

### 2. Style Selection
- **Corporate Style**: Professional business attire, neutral background, polished look suitable for LinkedIn and corporate profiles
- **Classic Style**: Timeless portrait style with soft lighting, traditional poses, elegant and sophisticated appearance

### 3. AI Headshot Generation
- Process uploaded photo using Google's Imagen API (image-to-image)
- Generate professional headshot based on selected style
- Display loading state during generation
- Handle API errors gracefully

### 4. Side-by-Side Comparison
- Display original photo and generated headshot side-by-side
- Enable easy comparison view
- Download option for generated headshot
- Option to regenerate with different style

## Technical Requirements

### Functional Requirements
1. User must be able to upload a single photo
2. System must validate image format and size
3. User must select one style before generation
4. System must call Google Imagen API with appropriate prompts
5. System must display both original and generated images
6. User must be able to download the generated headshot
7. System must handle errors and display user-friendly messages

### Non-Functional Requirements
1. **Performance**: Image generation should complete within 30 seconds
2. **Usability**: Intuitive UI with clear instructions
3. **Reliability**: Proper error handling and retry logic
4. **Security**: Secure API key management, image validation
5. **Responsiveness**: Works on desktop and tablet devices

## Tech Stack

### Frontend
- **Framework**: React 18+
- **Build Tool**: Vite
- **Styling**: CSS Modules / Tailwind CSS
- **HTTP Client**: Axios
- **State Management**: React Hooks (useState, useEffect)
- **File Upload**: HTML5 File API

### Backend
- **Framework**: Express.js
- **Runtime**: Node.js 18+
- **API Integration**: Google Imagen API
- **Middleware**:
  - `express.json()` for JSON parsing
  - `cors` for cross-origin requests
  - `multer` for file uploads
- **Environment Variables**: dotenv
- **Error Handling**: Custom error middleware

### APIs & Services
- **Google Imagen API**: Image-to-image generation
  - Documentation: https://ai.google.dev/gemini-api/docs/image-generation
  - Endpoint: Gemini API with image generation capabilities
  - Authentication: API Key

### Development Tools
- **Version Control**: Git
- **Package Manager**: npm
- **Code Editor**: VS Code (recommended)

## Project Structure

```
professional-headshot-app/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageUpload.jsx
│   │   │   ├── StyleSelector.jsx
│   │   │   ├── ImageComparison.jsx
│   │   │   └── LoadingSpinner.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── backend/
│   ├── src/
│   │   ├── routes/
│   │   │   └── headshot.js
│   │   ├── services/
│   │   │   └── imagenService.js
│   │   ├── middleware/
│   │   │   └── errorHandler.js
│   │   └── server.js
│   ├── .env.example
│   └── package.json
└── README.md
```

## Milestones

### Milestone 1: UI Setup and Frontend Development
**Duration**: 1 week
**Objective**: Build complete frontend interface with all UI components

#### Tasks
1. **Project Initialization**
   - Initialize React project with Vite
   - Initialize Express backend project
   - Set up project structure and dependencies
   - Configure CORS and basic Express middleware

2. **Image Upload Component**
   - Create file input with drag-and-drop support
   - Implement image preview functionality
   - Add client-side validation (format, size)
   - Display uploaded image with metadata

3. **Style Selector Component**
   - Create style selection UI (Corporate, Classic)
   - Display style descriptions and sample images
   - Implement selection state management
   - Add visual feedback for selected style

4. **Comparison View Component**
   - Build side-by-side image layout
   - Implement responsive design
   - Add download button for generated image
   - Create "Generate New" option

5. **Loading & Error States**
   - Design loading spinner/progress indicator
   - Create error message components
   - Implement user feedback mechanisms

#### Deliverables
- Fully functional frontend UI
- All components working with mock data
- Responsive design for desktop/tablet
- Basic Express server structure ready
- Mock API endpoints for testing frontend

---

### Milestone 2: Google Imagen API Integration
**Duration**: 1 week
**Objective**: Integrate Google Imagen API and complete full application flow

#### Tasks
1. **Google Cloud Setup**
   - Create Google Cloud project
   - Enable Gemini API with image generation
   - Generate and secure API key
   - Configure environment variables

2. **Backend API Endpoints**
   - Create `/api/generate-headshot` POST endpoint
   - Implement file upload handling with Multer
   - Add request validation middleware
   - Set up error handling middleware

3. **Imagen Service Integration**
   - Implement Google Imagen API client
   - Create style-specific prompts:
     - **Corporate**: "Transform this photo into a professional corporate headshot with business attire, neutral office background, professional lighting, high quality portrait"
     - **Classic**: "Transform this photo into a classic professional portrait with timeless style, soft lighting, elegant pose, traditional headshot photography"
   - Handle image-to-image transformation
   - Process API responses and return images

4. **Frontend-Backend Integration**
   - Connect frontend to backend API
   - Implement image upload to server
   - Handle API responses and display generated images
   - Add proper error handling and user feedback

5. **Testing & Refinement**
   - Test end-to-end flow with real images
   - Optimize API prompts for better results
   - Test error scenarios (network issues, API limits)
   - Performance testing and optimization
   - Fix bugs and improve UX

6. **Documentation & Deployment Preparation**
   - Document API endpoints
   - Create setup instructions
   - Add environment variable templates
   - Prepare deployment configuration

#### Deliverables
- Fully integrated application
- Working image generation with Google Imagen API
- Complete error handling
- Documentation for setup and deployment
- Production-ready codebase

## API Endpoint Specifications

### POST /api/generate-headshot

**Request**:
```
Content-Type: multipart/form-data

Fields:
- image: File (required) - The uploaded photo
- style: String (required) - Either "corporate" or "classic"
```

**Response** (Success):
```json
{
  "success": true,
  "data": {
    "originalImage": "base64_or_url",
    "generatedImage": "base64_or_url",
    "style": "corporate"
  }
}
```

**Response** (Error):
```json
{
  "success": false,
  "error": {
    "message": "Error message",
    "code": "ERROR_CODE"
  }
}
```

## Environment Variables

### Backend (.env)
```
PORT=3000
GOOGLE_API_KEY=your_google_api_key_here
MAX_FILE_SIZE=5242880
ALLOWED_FILE_TYPES=image/jpeg,image/png,image/webp
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:3000/api
```

## Security Considerations

1. **API Key Protection**: Never expose Google API key in frontend code
2. **File Validation**: Validate file types and sizes on both client and server
3. **Rate Limiting**: Implement rate limiting to prevent API abuse
4. **CORS Configuration**: Restrict CORS to specific origins in production
5. **Input Sanitization**: Sanitize all user inputs
6. **Error Messages**: Don't expose sensitive information in error messages

## Future Enhancements

1. **Additional Styles**: Add more headshot styles (Creative, Casual, Formal)
2. **Batch Processing**: Allow multiple photos to be processed at once
3. **User Accounts**: Save generated headshots to user profiles
4. **Advanced Editing**: Add post-generation editing tools (brightness, contrast, crop)
5. **Social Sharing**: Direct sharing to LinkedIn, social media
6. **Background Removal**: Option to remove/replace backgrounds
7. **Style Customization**: Let users customize style parameters
8. **History**: View and download previously generated headshots

## Success Metrics

1. Successfully generate headshots within 30 seconds
2. 95%+ API success rate
3. Support for images up to 5MB
4. Responsive UI on desktop and tablet
5. Clear error messages for all failure scenarios
6. User can complete full flow in under 2 minutes

---

**Version**: 1.0
**Last Updated**: November 11, 2025
**Status**: Ready for Development
