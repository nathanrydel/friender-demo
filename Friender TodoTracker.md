# Friender Todo Tracker

## Minimum Viable Product Stage

### Project Structure

- │ = ALT + 179
- └ = ALT + 192
- ├ = ALT + 195
- ─ = ALT + 196

``` arduino
Friender/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── home-anon.html
│   ├── login.html
│   ├── signup.html
│   └── profile.html
│
├── static/
│   └── css/
│       └── style.css
│
├── models.py
├── routes.py
├── forms.py
│
├── app.py
├── requirements.txt
└── README.md
```

### [ ] **Landing Page for Non-Logged-in Users**

- [ ] Create a landing page that welcomes users and provides basic information about the platform.
- [ ] Include a call-to-action button or link to the signup page.

### [ ] **Homepage for Logged-in Users**

- [ ] Develop a homepage layout for users who are logged in.
- [ ] Display relevant information or actions such as profile updates, friend suggestions, or recent activity.

### [ ] **Login Page**

- [ ] Design a login page with fields for username and password.
- [ ] Implement authentication logic to validate user credentials.
- [ ] Include a link to the signup page for new users.

### [ ] **Signup Page**

- [ ] Create a signup form with fields for username, password, email, phone number, friend radius, profile photo, first name, and last name.
- [ ] Implement form validation to ensure all required fields are filled.
- [ ] Set up logic to create a new user account upon submission.

### [ ] **Profile Page**

- [ ] Design a profile page layout displaying user information in a bootstrap card format.
- [ ] Include the user's profile photo, username, first name, last name, list of hobbies, list of interests, and an edit profile button.
- [ ] Ensure that only the profile owner can view and edit their profile.

### [ ] **Profile Edit Form**

- [ ] Create a form for users to edit their profile information.
- [ ] Allow users to upload additional photos, modify their friend radius, and add interests and hobbies from dropdown lists.
- [ ] Implement validation to handle edits appropriately.

### [ ] **Users Page**

- [ ] Develop a page to display cards of all users on the site.
- [ ] Each card should include the user's profile photo, username, first name, list of hobbies, and list of interests.
- [ ] Enable users to click on a card to navigate to the respective user's profile page.

### [ ] **Routing and Navigation**

- [ ] Set up routing logic to navigate between different pages of the application.
- [ ] Ensure proper redirection based on user actions such as login, signup, profile edit, etc.

### [ ] **Styling and UI Enhancement**

- [ ] Apply CSS styling to improve the visual appearance and user experience of the pages.
- [ ] Ensure consistency in design elements across the application.

### Notable Bugs
