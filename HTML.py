<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Taitan Bot Hosting</title>
    <style>
        /* --- CORE CSS (UNCHANGED) --- */
        :root { 
            --bg-deep: #111827; 
            --bg-card: #1f2937; 
            --text-primary: #f9fafb; 
            --text-secondary: #9ca3af; 
            --border-color: #374151; 
            --accent-blue: #3b82f6; 
            --accent-green: #22c55e; 
            --accent-red: #ef4444; 
            --accent-amber: #f59e0b; 
            --accent-teal: #14b8a6; 
            --console-bg: #000000; 
            --console-text: #6ee7b7; 
            --shadow-dark: rgba(0, 0, 0, 0.4); 
        } 
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; 
            background-color: var(--bg-deep); 
            color: var(--text-primary); 
            margin: 0; 
            padding: 10px; 
            -ms-overflow-style: none;
            scrollbar-width: none;
        } 
        body::-webkit-scrollbar {
            display: none;
        }

        /* --- Login Screen Styling (FIXED POSITIONING FOR NO SCROLL) --- */
        #login-screen {
            position: fixed; 
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex; 
            justify-content: center;
            align-items: center; 
            background-color: var(--bg-deep); 
            z-index: 9999;
        }

        .container { 
            max-width: 750px; 
            margin: 0 auto; 
            background-color: var(--bg-card); 
            border-radius: 10px; 
            box-shadow: 0 8px 25px var(--shadow-dark); 
            border: 1px solid var(--border-color); 
            padding: 20px; 
            margin-top: 15px; 
        } 
        
        .login-container { 
            max-width: 400px; 
            width: 100%;
            margin: 0 10px;
            display: flex; 
            flex-direction: column;
            gap: 15px;
            background-color: var(--bg-card); 
            border-radius: 10px; 
            box-shadow: 0 8px 25px var(--shadow-dark); 
            border: 1px solid var(--border-color); 
            padding: 20px; 
            
        }

        /* --- ERROR MESSAGE STYLE (POP-UP REPLACEMENT) --- */
        .error-message {
            background-color: rgba(239, 68, 68, 0.15);
            color: var(--accent-red); 
            border: 1px solid var(--accent-red);
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-size: 0.9em;
            font-weight: 500;
            display: none; 
        }
        
        /* ... (Rest of the CSS) ... */
        h1 { 
            color: var(--text-primary); 
            text-align: center; 
            margin-top: 0; 
            margin-bottom: 8px; 
            font-size: 1.9em; 
            font-weight: 700; 
            letter-spacing: -0.5px; 
        } 
        h1 span { 
            color: var(--accent-blue); 
        } 
        h2 { 
            color: var(--text-primary); 
            margin-top: 25px; 
            margin-bottom: 12px; 
            border-bottom: 1px solid var(--border-color); 
            padding-bottom: 6px; 
            font-size: 1.3em; 
            font-weight: 600; 
        } 
        .info-bar { 
            display: flex; 
            flex-wrap: wrap; 
            justify-content: space-between; 
            align-items: center; 
            gap: 10px; 
            padding: 10px 15px; 
            background-color: rgba(0,0,0,0.2); 
            border-radius: 8px; 
            margin-bottom: 18px; 
            border-left: 4px solid var(--accent-blue); 
            font-size: 0.95em; 
        } 
        .info-bar p { 
            margin: 0; 
        } 
        .status-indicator { 
            display: flex; 
            align-items: center; 
            gap: 8px; 
        } 
        .status-indicator::before { 
            content: ''; 
            display: inline-block; 
            width: 10px; 
            height: 10px; 
            border-radius: 50%; 
            animation: pulse 2s infinite; 
        } 
        .status-running { 
            color: var(--accent-green); 
            font-weight: 700; 
        } 
        .status-running::before { 
            background-color: var(--accent-green); 
            box-shadow: 0 0 7px var(--accent-green); 
        } 
        .status-stopped { 
            color: var(--accent-red); 
            font-weight: 700; 
        } 
        .status-stopped::before { 
            background-color: var(--accent-red); 
            box-shadow: 0 0 7px var(--accent-red); 
            animation: none; 
        } 
        .current-bot-name { 
            font-family: monospace; 
            background-color: var(--bg-deep); 
            padding: 3px 8px; 
            border-radius: 5px; 
            color: var(--accent-blue); 
        } 
        @keyframes pulse { 
            0% { opacity: 1; } 
            50% { opacity: 0.5; } 
            100% { opacity: 1; } 
        } 
        .control-panel { 
            background-color: rgba(0,0,0,0.15); 
            padding: 15px; 
            border-radius: 8px;
            border: 1px solid var(--border-color); 
            display: flex; 
            flex-direction: column;
            gap: 12px; 
            margin-bottom: 15px;
        }
        .control-section { 
            display: flex; 
            flex-direction: column; 
            gap: 8px; 
        }
        .control-section form { 
            display: flex; 
            flex-direction: column; 
            gap: 8px; 
        }
        .button-group { 
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 8px; 
        }
        /* Log control to use 3 columns */
        .log-controls-group {
             display: grid; 
             grid-template-columns: 1fr 1.3fr 1fr; /* Custom width for middle button (Copy Logs) */
             gap: 8px; 
        }
        /* END UPDATED */

        input[type="file"], input[type="text"], 
        input[type="email"], input[type="password"] {
            padding: 9px 10px; 
            width: 100%; 
            box-sizing: border-box; 
            border-radius: 5px;
            border: 1px solid var(--border-color); 
            background-color: var(--bg-deep);
            color: var(--text-primary); 
            font-size: 0.95em; 
            transition: all 0.2s;
        }
        input:focus {
            border-color: var(--accent-blue); 
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3); 
            outline: none;
        }
        input[type="file"]::file-selector-button {
            background-color: var(--accent-blue); 
            color: white; 
            border: none; 
            padding: 7px 10px;
            border-radius: 4px; 
            cursor: pointer; 
            transition: background-color 0.2s; 
            margin-right: 10px;
        }
        input[type="file"]::file-selector-button:hover { 
            background-color: #2563eb; 
        }
        button, .btn-link {
            padding: 9px 10px; 
            border: none; 
            border-radius: 5px; 
            font-weight: 600; 
            cursor: pointer;
            transition: all 0.2s ease; 
            text-transform: uppercase; 
            font-size: 0.8em; 
            letter-spacing: 0.5px;
            box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2); 
            color: #fff; 
            text-decoration: none; 
            text-align: center;
            display: flex; 
            align-items: center; 
            justify-content: center; 
            gap: 6px;
        }
        button:hover, .btn-link:hover { 
            transform: translateY(-1px); 
            box-shadow: 0 5px 8px rgba(0, 0, 0, 0.3); 
        }
        button:active, .btn-link:active { 
            transform: translateY(0); 
            box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2); 
        }
        button:disabled { 
            opacity: 0.5; 
            cursor: not-allowed; 
            transform: none; 
            box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2); 
        }
        .btn-upload { background-color: var(--accent-blue); } 
        .btn-upload:hover { background-color: #2563eb; }
        .btn-start { background-color: var(--accent-green); } 
        .btn-start:hover { background-color: #16a3a; }
        .btn-stop { background-color: var(--accent-red); } 
        .btn-stop:hover { background-color: #dc2626; }
        .btn-pip { background-color: var(--accent-amber); } 
        .btn-pip:hover { background-color: #d97706; }
        .btn-contact { background-color: var(--accent-teal); display: block; margin-bottom: 25px; }
        .btn-contact:hover { background-color: #0d9488; }
        
        /* NEW STYLE FOR LOGIN PAGE CONTACT BUTTON & GOOGLE BUTTON */
        .btn-google, .btn-contact-login {
            padding: 10px 10px; 
            font-size: 0.9em; 
            letter-spacing: 0.5px;
            width: 100%; 
            box-sizing: border-box; 
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            text-transform: uppercase;
        }

        .btn-secondary {
            background-color: #4b5563; 
            box-shadow: none; 
            padding: 9px 10px; /* SAME HEIGHT AS OTHERS */
            font-size: 0.8em; /* SAME FONT SIZE AS OTHERS */
        }
        .btn-secondary:hover { 
            background-color: #6b7280; 
            transform: translateY(-1px); /* APPLY HOVER EFFECT */
            box-shadow: 0 5px 8px rgba(0, 0, 0, 0.3);
        }
        /* Specific style for copy logs button (using btn-secondary color but custom grid column width) */
        .btn-copy-logs {
            background-color: #7c3aed; /* Violet shade */
            box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2);
        }
        .btn-copy-logs:hover {
            background-color: #6d28d9;
        }
        
        /* OLD: Professional small Copy Button Style (REMOVED) */
        #copy-button-small { display: none !important; }

        /* Console styling updated for relative positioning of copy button */
        .log-container {
            position: relative;
        }

        pre#logs {
            background-color: var(--console-bg); 
            color: var(--console-text); 
            padding: 12px; 
            border-radius: 6px;
            overflow-y: scroll; 
            height: 330px; 
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.85em; 
            white-space: pre-wrap; 
            word-break: break-all;
            border: 1px solid var(--border-color); 
            box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.5);
        }
        /* --- CENTERED LOG CONTROLS --- */
        .log-controls {
            margin-top: 12px; 
            display: flex; 
            justify-content: center; 
            gap: 10px;
        }
        /* Log controls to use the grid group */
        .log-controls .log-controls-group button { 
            width: 100%; 
        }
        .log-controls .log-controls-group { 
            width: 100%;
        }
        /* END UPDATED */
        
        footer {
            text-align: center; 
            margin-top: 25px; 
            padding-top: 12px;
            border-top: 1px solid var(--border-color); 
            font-size: 0.85em; 
            color: var(--text-secondary);
        }
        /* --- LOGIN CSS --- */
        .login-form-group {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .btn-google {
            background-color: #db4437; 
            margin-top: 5px;
        }
        .btn-google:hover {
            background-color: #c33d30;
        }
        .btn-contact-login { 
            background-color: var(--accent-teal); 
            margin-top: 10px;
        }
        .btn-contact-login:hover { 
            background-color: #0d9488;
        }

        .switch-text {
            text-align: center;
            font-size: 0.9em;
            color: var(--text-secondary);
        }
        .switch-link {
            color: var(--accent-blue);
            cursor: pointer;
            text-decoration: none;
            font-weight: 600;
        }
        .switch-link:hover {
            text-decoration: underline;
        }
        .btn-logout { 
            background-color: var(--accent-red); 
            margin-top: 0;
        }
        .btn-logout:hover {
             background-color: #dc2626;
        }

        /* SUCCESS MESSAGE STYLE (HIDDEN PER USER REQUEST) */
        #copy-success-message {
            display: none !important;
        }

        /* (Removed Keyframes associated with success message) */
        
    </style>
</head>
<body>
    
    <div id="copy-success-message">Logs Copied!</div> <div id="login-screen" style="display: flex;">
        <div class="login-container">
            <h1>PRO BOT <span id="auth-title">LOGIN</span></h1>
            
            <div id="auth-error-message" class="error-message"></div>

            <form id="auth-form" class="login-form-group">
                <input type="email" id="email" placeholder="Email Address" required>
                <input type="password" id="password" placeholder="Password" required>
                
                <button type="submit" id="auth-button" class="btn-upload"><i class="fas fa-sign-in-alt"></i> LOGIN</button>
            </form>
            
            <div class="switch-text">
                <span id="switch-prompt">Don't have an account?</span> 
                <a href="#" id="switch-mode" class="switch-link">Register Here</a>
            </div>
            
            <hr style="border-color: var(--border-color); margin: 20px 0 15px 0;">
            
            <button id="google-login" class="btn-google"><i class="fab fa-google"></i> Sign in with Google</button>
            
            <a href="https://t.me/oxmzoo" target="_blank" class="btn-link btn-contact-login"><i class="fab fa-telegram-plane"></i> DEVELOPER CONTACT</a>
        </div>
    </div>


    <div id="dashboard-content" class="container" style="display: none;">
        <h1>PRO BOT <span>DASHBOARD</span></h1>
        
        <div class="info-bar">
            <div class="status-indicator">
                Status: <span id="status" class="status-{{ status.lower() }}">{{ status.upper() }}</span>
            </div>
            <p>Loaded: <span id="current-bot-name-display" class="current-bot-name">{{ bot_file if bot_file else "None" }}</span></p>
        </div>

        <div class="control-panel">
            <div class="control-section">
                <h2>Upload & Unpack .ZIP</h2>
                <form id="upload-form" onsubmit="handleUpload(event)">
                    <input type="file" name="botzip" accept=".zip" required>
                    <button type="submit" class="btn-upload"><i class="fas fa-upload"></i> Upload & Replace</button>
                </form>
            </div>

            <div class="control-section">
                <h2>Bot Control</h2>
                <div class="button-group">
                    <button class="btn-start" onclick="sendControlAction('/start')"><i class="fas fa-play"></i> START</button>
                    <button class="btn-stop" onclick="sendControlAction('/stop')"><i class="fas fa-stop"></i> STOP</button>
                </div>
            </div>

            <div class="control-section">
                <h2>PIP Install</h2>
                <form id="pip-form" onsubmit="handlePipInstall(event)">
                    <input type="text" name="package_name" placeholder="e.g., requests, telethon" required>
                    <button type="submit" class="btn-pip"><i class="fas fa-hammer"></i> Install Package</button>
                </form>
            </div>
            
            <div class="button-group">
                <a href="https://t.me/oxmzoo" target="_blank" class="btn-link btn-contact" style="margin-bottom: 0;"><i class="fas fa-headset"></i> DEVELOPER CONTACT</a>
                <button class="btn-logout" onclick="handleLogout()"><i class="fas fa-sign-out-alt"></i> LOGOUT</button>
            </div>
        </div>

        <h2>REAL-TIME CONSOLE LOGS</h2>
        <div class="log-container">
            <pre id="logs">{{ logfile }}</pre>
        </div>
        
        <div class="log-controls">
            <div class="log-controls-group">
                <button class="btn-secondary" onclick="sendControlAction('/clear')"><i class="fas fa-eraser"></i> Clear Console</button>
                <button class="btn-secondary btn-copy-logs" onclick="copyLogsToClipboard()"><i class="fas fa-copy"></i> Copy Logs</button> <button class="btn-secondary" onclick="refreshLogs(true)"><i class="fas fa-sync-alt"></i> Manual Refresh</button>
            </div>
        </div>

        <footer>
            &copy; 2025 Taitan. All rights reserved.
        </footer>
    </div>

    <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-auth-compat.js"></script>

    <script>
        
        // Load Font Awesome icons for better visuals
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css';
        document.head.appendChild(link);
        
        // --- 1. FIREBASE CONFIGURATION ---
        const firebaseConfig = {
          apiKey: "AIzaSyAXi1qM4yuyHG9o5f2VnD29yfsrMqMolCk",
          authDomain: "chatting-app-8865d.firebaseapp.com",
          projectId: "chatting-app-8865d",
          storageBucket: "chatting-app-8865d.firebasestorage.app",
        };

        const app = firebase.initializeApp(firebaseConfig);
        const auth = firebase.auth();
        const googleProvider = new firebase.auth.GoogleAuthProvider();

        // --- 2. AUTH-SPECIFIC DOM ELEMENTS ---
        const loginScreen = document.getElementById('login-screen');
        const dashboardContent = document.getElementById('dashboard-content');
        
        const form = document.getElementById('auth-form');
        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('password');
        const authButton = document.getElementById('auth-button');
        const authTitle = document.getElementById('auth-title');
        const switchModeLink = document.getElementById('switch-mode');
        const switchPrompt = document.getElementById('switch-prompt');
        const googleLoginButton = document.getElementById('google-login');
        const authErrorDisplay = document.getElementById('auth-error-message'); 
        // const copySuccessMessage = document.getElementById('copy-success-message'); // Removed from variable to avoid usage

        let isLoginMode = true;
        
        // --- CRITICAL PERSISTENCE KEY (MUST MATCH PYTHON'S USER_ID_COOKIE) ---
        const LOCAL_STORAGE_KEY = 'titan_bot_firebase_uid'; 
        
        // NEW: Global variable to store the current, correct UID (Firebase UID or temporary client_uuid)
        let CURRENT_FIREBASE_UID = '{{ user_id }}'; 

        // --- Error Message Helper (For both Login and Dashboard) ---
        function displayAuthError(message) {
            authErrorDisplay.textContent = message;
            authErrorDisplay.style.display = 'block';
            passwordInput.value = ''; 
            setTimeout(() => {
                authErrorDisplay.style.display = 'none';
            }, 5000); 
        }

        // --- 3. AUTH LOGIC ---

        function handleLogout() {
            // if (!confirm('Are you sure you want to log out?')) return; // Confirmation pop-up removed
            auth.signOut().then(() => {
                console.log("Logged out successfully.");
            }).catch((error) => {
                displayAuthError("Logout Error: " + error.message); 
            });
        }

        // UI Toggle Logic (Login <-> Register)
        switchModeLink.addEventListener('click', (e) => {
            e.preventDefault();
            isLoginMode = !isLoginMode;
            authErrorDisplay.style.display = 'none';
            
            if (isLoginMode) {
                authButton.innerHTML = '<i class="fas fa-sign-in-alt"></i> LOGIN';
                switchModeLink.textContent = 'Register Here';
                switchPrompt.textContent = "Don't have an account?";
                authTitle.textContent = 'LOGIN';
            } else {
                authButton.innerHTML = '<i class="fas fa-user-plus"></i> REGISTER';
                switchModeLink.textContent = 'Login Here';
                switchPrompt.textContent = "Already have an account?";
                authTitle.textContent = 'REGISTER';
            }
        });

        // Email/Password Submission Handler
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            setInteractions(true);
            authErrorDisplay.style.display = 'none'; 
            const email = emailInput.value;
            const password = passwordInput.value;

            try {
                if (isLoginMode) {
                    await auth.signInWithEmailAndPassword(email, password);
                } else {
                    await auth.createUserWithEmailAndPassword(email, password);
                }
            } catch (error) {
                console.error("Auth Error:", error);
                
                let userMessage = error.message;
                
                if (error.code === 'auth/operation-not-allowed') {
                    userMessage = "Email/Password login is NOT ENABLED. Please enable it in Firebase Console -> Authentication -> Sign-in Method.";
                } else if (error.code === 'auth/invalid-credential' || error.code === 'auth/wrong-password' || error.code === 'auth/user-not-found') {
                    userMessage = "Invalid Email or Password. Please check your credentials or register.";
                }
                
                displayAuthError(userMessage);
                setInteractions(false);
            }
        });

        // Google Login Handler
        googleLoginButton.addEventListener('click', async () => {
            setInteractions(true);
            authErrorDisplay.style.display = 'none'; 
            try {
                await auth.signInWithPopup(googleProvider);
            } catch (error) {
                console.error("Google Auth Error:", error);
                displayAuthError("Google Sign-in Failed. Error: " + error.message);
            } finally {
                setInteractions(false);
            }
        });

        // --- 4. AUTH STATE LISTENER (Triggers UI switch and dashboard setup) ---
        let dashboardInitialized = false;
        auth.onAuthStateChanged(user => {
            if (user) {
                // User is LOGGED IN: Use Firebase UID for persistence
                
                const firebaseUid = user.uid;
                
                // CRITICAL: Update the global variable
                CURRENT_FIREBASE_UID = firebaseUid; 

                localStorage.setItem(LOCAL_STORAGE_KEY, firebaseUid);
                setCookie(LOCAL_STORAGE_KEY, firebaseUid, 365); 
                
                loginScreen.style.display = 'none';
                dashboardContent.style.display = 'block';
                
                if (!dashboardInitialized) {
                    // Start Dashboard background tasks only once
                    refreshLogs(true); 
                    setInterval(refreshLogs, 1500); 
                    dashboardInitialized = true;
                }
                
            } else {
                // User is LOGGED OUT: Show Login Screen
                dashboardContent.style.display = 'none';
                loginScreen.style.display = 'flex'; 
                
                // IMPORTANT: When logged out, fall back to the initial server-assigned ID for non-auth requests
                CURRENT_FIREBASE_UID = '{{ user_id }}';
                
                // Clear client-side ID 
                localStorage.removeItem(LOCAL_STORAGE_KEY); 
                setCookie(LOCAL_STORAGE_KEY, '', -1); // Clear cookie
            }
            setInteractions(false);
        });


        // --- 5. DASHBOARD FUNCTIONS (API calls updated to send X-User-ID header) ---
        
        function setCookie(name, value, days) {
            let expires = "";
            if (days) {
                const date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toUTCString();
            }
            document.cookie = name + "=" + (value || "")  + expires + "; path=/; SameSite=Lax"; 
        }

        // NEW: Helper function for all API calls to inject the UID header
        function fetchWithUID(url, options = {}) {
            const defaultHeaders = {
                // Send the correct UID in a custom header. The Flask backend prioritizes this.
                'X-User-ID': CURRENT_FIREBASE_UID 
            };

            // Combine default and provided headers
            options.headers = {
                ...defaultHeaders,
                ...options.headers 
            };
            
            // For file uploads (FormData), manually setting Content-Type is wrong, so we delete it if body is FormData
            if (options.body instanceof FormData) {
                delete options.headers['Content-Type']; 
            }
            
            return fetch(url, options);
        }
        
        const logsElement = document.getElementById('logs');
        
        function refreshLogs(forceScroll = false){
            if (dashboardContent.style.display !== 'block') return; 
            
            // Use fetchWithUID
            fetchWithUID('/logs').then(r => r.text()).then(data => {
                const isScrolledToBottom = logsElement.scrollHeight - logsElement.scrollTop - logsElement.clientHeight < 20;
                logsElement.textContent = data;
                if (forceScroll || isScrolledToBottom) {
                    logsElement.scrollTop = logsElement.scrollHeight;
                }
            }).catch(e => console.error("Could not fetch logs:", e));

            // Use fetchWithUID
            fetchWithUID('/status').then(r => r.json()).then(data => {
                const statusElement = document.getElementById('status');
                const botNameElement = document.getElementById('current-bot-name-display');
                
                const newStatus = data.status.toUpperCase();
                const newBotName = data.bot_file || "None";
                
                if (statusElement.textContent.trim() !== newStatus) {
                    statusElement.textContent = newStatus;
                    statusElement.className = 'status-' + data.status;
                }
                
                if (botNameElement.textContent.trim() !== newBotName) {
                    botNameElement.textContent = newBotName;
                }
            }).catch(e => console.error("Could not fetch status:", e));
        }

        function setInteractions(disabled) {
            // Re-enabling buttons immediately after setInteractions(true) call was causing the issue.
            // This function is generally used for submission states (e.g., login, upload, start/stop).
            document.querySelectorAll('button, input').forEach(el => el.disabled = disabled);
            document.querySelectorAll('.btn-link').forEach(el => {
                el.style.pointerEvents = disabled ? 'none' : 'auto';
                el.style.opacity = disabled ? '0.5' : '1';
            });
        }
        
        // FIX APPLIED: Button functionality fixed and success message removal implemented.
        function copyLogsToClipboard() {
            const logContent = logsElement.textContent;
            
            // Check for modern Clipboard API support
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(logContent).then(() => {
                    // SUCCESS: Do nothing (User requested no success message)
                }).catch(err => {
                    console.error('Failed to copy text (Clipboard API error): ', err);
                    displayAuthError('Failed to copy logs. Check browser permissions or try using an updated browser.');
                });
            } else {
                // Fallback for older browsers (less reliable)
                try {
                    const tempTextArea = document.createElement('textarea');
                    tempTextArea.value = logContent;
                    tempTextArea.style.position = 'fixed'; // Hide off-screen
                    tempTextArea.style.opacity = 0;
                    document.body.appendChild(tempTextArea);
                    tempTextArea.focus();
                    tempTextArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(tempTextArea);
                    
                    // SUCCESS: Do nothing (User requested no success message)
                } catch (err) {
                    console.error('Failed to copy text (Fallback error): ', err);
                    displayAuthError('Failed to copy logs to clipboard. Fallback method failed.');
                }
            }
        }
        // END FIX

        function sendControlAction(url) {
            if (url === '/start' && document.getElementById('status').textContent.trim() === 'RUNNING') {
                displayAuthError('Bot is already running.');
                return;
            }
            setInteractions(true);
            // Use fetchWithUID
            fetchWithUID(url, { method: 'POST' }).then(r => r.json()).then(data => {
                if(data.message) console.log(data.message);
                refreshLogs(true);
            }).catch(e => displayAuthError('Error: ' + e.message)).finally(() => setTimeout(() => setInteractions(false), 500));
        }

        function handleUpload(event) {
            event.preventDefault();
            const form = document.getElementById('upload-form');
            const formData = new FormData(form);
            const fileInput = formData.get('botzip');
            
            if (!fileInput || fileInput.name === '') {
                displayAuthError('Please select a ZIP file to upload.');
                return;
            }

            setInteractions(true);
            // Use fetchWithUID
            fetchWithUID('/upload', { method: 'POST', body: formData }).then(r => r.json()).then(data => {
                console.log(data.message);
                form.reset();
                refreshLogs(true);
            }).catch(e => displayAuthError('Error: ' + e.message)).finally(() => setTimeout(() => setInteractions(false), 500));
        }

        function handlePipInstall(event) {
            event.preventDefault();
            const form = document.getElementById('pip-form');
            const formData = new FormData(form);
            const packageName = formData.get('package_name').trim();

            if (!packageName) {
                displayAuthError('Package name is required!');
                return;
            }

            setInteractions(true);
            // Use fetchWithUID
            fetchWithUID('/pip_install', { 
                method: 'POST', 
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: new URLSearchParams(formData)
            }).then(r => r.json()).then(data => {
                console.log(data.message);
                form.reset();
                refreshLogs(true);
            }).catch(e => displayAuthError('Error: ' + e.message)).finally(() => setTimeout(() => setInteractions(false), 500));
        }

        document.addEventListener('DOMContentLoaded', () => {
            // Initial check to load UID if it was stored from a previous visit
            const storedUid = localStorage.getItem(LOCAL_STORAGE_KEY);
            if (storedUid) {
                 CURRENT_FIREBASE_UID = storedUid;
            }
        });
    </script>
</body>
</html>