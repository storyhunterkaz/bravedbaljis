// Configuration
const CLIENT_ID = '1SmSroC8Ouk9lPg55xOQ836kJ'; // Your X Client ID
const REDIRECT_URI = 'http://localhost:3000/callback'; // Make sure this matches your X app's callback URL
const SCOPES = ['tweet.read', 'users.read', 'offline.access'];

// Note: Client Secret should NEVER be exposed in client-side code
// It will be used in the server-side implementation of exchangeCodeForToken()

// Helper function to generate a random string for code verifier
function generateCodeVerifier() {
    const array = new Uint8Array(32);
    window.crypto.getRandomValues(array);
    return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
}

// Helper function to generate code challenge from verifier
async function generateCodeChallenge(verifier) {
    const encoder = new TextEncoder();
    const data = encoder.encode(verifier);
    const hash = await window.crypto.subtle.digest('SHA-256', data);
    return btoa(String.fromCharCode(...new Uint8Array(hash)))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=+$/, '');
}

// Generate random state for CSRF protection
function generateState() {
    const array = new Uint8Array(16);
    window.crypto.getRandomValues(array);
    return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
}

// Redirect to X authorization page
async function redirectToXAuth() {
    const codeVerifier = generateCodeVerifier();
    const codeChallenge = await generateCodeChallenge(codeVerifier);
    const state = generateState();

    // Store code verifier and state in session storage
    sessionStorage.setItem('code_verifier', codeVerifier);
    sessionStorage.setItem('state', state);

    // Construct authorization URL
    const authUrl = new URL('https://twitter.com/i/oauth2/authorize');
    authUrl.searchParams.append('response_type', 'code');
    authUrl.searchParams.append('client_id', CLIENT_ID);
    authUrl.searchParams.append('redirect_uri', REDIRECT_URI);
    authUrl.searchParams.append('scope', SCOPES.join(' '));
    authUrl.searchParams.append('state', state);
    authUrl.searchParams.append('code_challenge', codeChallenge);
    authUrl.searchParams.append('code_challenge_method', 'S256');

    // Redirect to X authorization page
    window.location.href = authUrl.toString();
}

// Handle the callback from X
async function handleXCallback() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');
    const state = urlParams.get('state');
    const storedState = sessionStorage.getItem('state');
    const codeVerifier = sessionStorage.getItem('code_verifier');

    if (!code || !state || !storedState || !codeVerifier) {
        console.error('Missing required parameters');
        return;
    }

    if (state !== storedState) {
        console.error('State mismatch - possible CSRF attack');
        return;
    }

    try {
        const tokenData = await exchangeCodeForToken(code, codeVerifier);
        await fetchXUserProfile(tokenData.access_token);
    } catch (error) {
        console.error('Error during authentication:', error);
    }
}

// Simulate token exchange (to be replaced with actual server-side implementation)
async function exchangeCodeForToken(authCode, codeVerifier) {
    console.log('Would make POST request to https://api.twitter.com/2/oauth2/token with:');
    console.log({
        grant_type: 'authorization_code',
        code: authCode,
        redirect_uri: REDIRECT_URI,
        code_verifier: codeVerifier,
        client_id: CLIENT_ID
    });
    console.log('// TODO: Implement actual server-side call here to securely exchange code for token and fetch user data');

    // Return mock token for testing
    return {
        access_token: 'mock_access_token_for_testing',
        user_id: 'mock_user_id'
    };
}

// Fetch user profile from X
async function fetchXUserProfile(accessToken) {
    try {
        const response = await fetch('https://api.twitter.com/2/users/me', {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch user profile');
        }

        const data = await response.json();
        displayUserProfile(data);
        displayToken(accessToken);
    } catch (error) {
        console.error('Error fetching user profile:', error);
    }
}

// Display user profile information
function displayUserProfile(profileData) {
    const profileDisplay = document.getElementById('profileDisplay');
    profileDisplay.innerHTML = `
        <h2>Welcome, ${profileData.data.username}!</h2>
        <img src="${profileData.data.profile_image_url}" alt="Profile" style="width: 100px; height: 100px; border-radius: 50%;">
    `;
}

// Display token (for debugging)
function displayToken(token) {
    const tokenDisplay = document.getElementById('tokenDisplay');
    tokenDisplay.textContent = `Access Token: ${token}`;
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    const connectButton = document.getElementById('connectXButton');
    connectButton.addEventListener('click', redirectToXAuth);

    // Check if we're on the callback page
    if (window.location.pathname === '/callback') {
        handleXCallback();
    }
}); 