const API_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
    ? 'http://localhost:8000' 
    : '/api'; // Standard Vercel API routing

window.onload = () => {
    initLoginSequence();
    initMatrix();
    fetchModules();
    fetchLabHistory();
    initHUD();
    initDataParticles();
    initAttackMap();
    checkApiStatus();

    const runBtn = document.getElementById('run-btn');
    if (runBtn) {
        runBtn.addEventListener('click', executeTool);
    }
};

function switchTheme(theme) {
    document.body.classList.remove('theme-neon', 'theme-retro');
    if (theme === 'neon') document.body.classList.add('theme-neon');
    else if (theme === 'retro') document.body.classList.add('theme-retro');
    initMatrix();
}

function triggerPanic() {
    const overlay = document.getElementById('panic-overlay');
    overlay.style.display = 'block';
    document.body.style.animation = 'glitch 0.05s infinite';
    setTimeout(() => {
        overlay.style.display = 'none';
        document.body.style.animation = 'none';
    }, 2000);
}

async function submitContactForm() {
    const name = document.getElementById('contact-name').value;
    const email = document.getElementById('contact-email').value;
    const message = document.getElementById('contact-message').value;
    const statusEl = document.getElementById('contact-status');
    const form = document.getElementById('contact-form');
    
    if (!name || !email || !message) return;

    statusEl.style.color = 'var(--accent-primary)';
    statusEl.innerText = "[ ENCRYPTING_DATA... ]";
    form.classList.add('glitch');

    try {
        const response = await fetch(`${API_URL}/contact`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, message })
        });

        const data = await response.json();
        
        // Sequence of cool messages
        const steps = ["[ SIGNAL_LOCKED ]", "[ TRANSMITTING_BURST... ]", data.message];
        for (let s of steps) {
            statusEl.innerText = s;
            await new Promise(r => setTimeout(r, 800));
        }
        
        statusEl.style.color = 'var(--accent-secondary)';
        form.reset();
    } catch (error) {
        statusEl.style.color = 'var(--accent-red)';
        statusEl.innerText = "[ TRANSMISSION_FAILED ] Link offline.";
    } finally {
        form.classList.remove('glitch');
    }
}

function initAttackMap() {
    const canvas = document.getElementById('attack-map');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const pingCountEl = document.getElementById('ping-count');
    let pings = 0;

    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    const circles = [];

    function drawMap() {
        ctx.fillStyle = '#000';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.fillStyle = '#111';
        for (let i = 0; i < canvas.width; i += 20) {
            for (let j = 0; j < canvas.height; j += 20) {
                if (Math.random() > 0.4) ctx.fillRect(i, j, 2, 2);
            }
        }

        circles.forEach((c, index) => {
            ctx.beginPath();
            ctx.arc(c.x, c.y, c.r, 0, Math.PI * 2);
            ctx.strokeStyle = `rgba(0, 247, 255, ${c.a})`;
            ctx.lineWidth = 2;
            ctx.stroke();
            
            c.r += 2;
            c.a -= 0.02;

            if (c.a <= 0) circles.splice(index, 1);
        });

        requestAnimationFrame(drawMap);
    }

    setInterval(() => {
        circles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: 5,
            a: 1
        });
        pings++;
        pingCountEl.textContent = pings;
    }, 800);

    drawMap();
}

function initLoginSequence() {
    const log = document.getElementById('boot-log');
    const overlay = document.getElementById('login-overlay');
    const btn = document.getElementById('boot-btn');
    
    if (!log || !overlay || !btn) return;

    const messages = [
        "[ OK ] Mounting local filesystems...",
        "[ OK ] Initializing Secure Kernel...",
        "[ OK ] Starting Cryptographic Engine...",
        "[ OK ] Connecting to Global Threat Feed...",
        "[ OK ] 24 Lab Modules Verified.",
        "[ OK ] Matrix Background Initialized.",
        "[ WARN ] Unauthorized access attempt from 10.4.x.x detected and logged.",
        "[ OK ] CYBERHARI PROTOCOL ACTIVE.",
        "READY FOR AUTHENTICATION..."
    ];

    let i = 0;
    const interval = setInterval(() => {
        if (i < messages.length) {
            const line = document.createElement('div');
            line.textContent = messages[i];
            log.appendChild(line);
            log.scrollTop = log.scrollHeight;
            i++;
        } else {
            clearInterval(interval);
        }
    }, 200);

    btn.onclick = () => {
        overlay.classList.add('hidden');
        setTimeout(() => overlay.remove(), 1000);
    };
}

function initHUD() {
    const netlink = document.getElementById('hud-netlink');
    const graph = document.getElementById('hud-cpu-graph');
    const syslog = document.getElementById('hud-syslog');

    if (netlink) {
        setInterval(() => {
            const val = Math.floor(Math.random() * 20) + 80;
            netlink.textContent = val + "%";
        }, 2000);
    }

    if (graph) {
        for (let i = 0; i < 20; i++) {
            const bar = document.createElement('div');
            bar.className = 'graph-bar';
            graph.appendChild(bar);
        }

        setInterval(() => {
            const bars = graph.querySelectorAll('.graph-bar');
            bars.forEach(bar => {
                const h = Math.floor(Math.random() * 40) + 5;
                bar.style.height = h + "px";
            });
        }, 500);
    }

    if (syslog) {
        const logs = ["KERNEL: OK", "FS_CHK: PASS", "API_LINK: UP", "MOD_SCAN: 24", "DB_WRITE: 0ms"];
        setInterval(() => {
            syslog.textContent = logs[Math.floor(Math.random() * logs.length)];
        }, 1500);
    }
}

function initDataParticles() {
    const container = document.body;
    const hex = "0123456789ABCDEF";
    
    setInterval(() => {
        const p = document.createElement('div');
        p.className = 'floating-data';
        p.style.left = Math.random() * 100 + "vw";
        p.style.animationDuration = (Math.random() * 10 + 10) + "s";
        let str = "";
        for(let i=0; i<8; i++) str += hex[Math.floor(Math.random()*16)];
        p.textContent = "0x" + str;
        container.appendChild(p);
        
        setTimeout(() => {
            if (p.parentNode) p.remove();
        }, 20000);
    }, 2000);
}

async function fetchLabHistory() {
    const container = document.getElementById('history-container');
    if (!container) return;
    try {
        const response = await fetch(`${API_URL}/lab-history`);
        const history = await response.json();
        
        if (history.length === 0) return;
        
        container.innerHTML = '';
        history.forEach(item => {
            const time = new Date(item.timestamp).toLocaleString();
            const div = document.createElement('div');
            div.className = 'card';
            div.style.padding = '1rem 1.5rem';
            div.style.marginBottom = '0';
            div.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="color: var(--accent-secondary); font-weight: bold;">[${item.tool.toUpperCase()}]</span>
                        <span style="color: var(--text-main); margin-left: 10px;">Target: ${item.target}</span>
                    </div>
                    <span style="color: var(--text-dim); font-size: 0.8rem;">${time}</span>
                </div>
            `;
            div.onclick = () => {
                const outputEl = document.getElementById('terminal-output');
                if (outputEl) {
                    outputEl.innerHTML = '';
                    typeToTerminal(`[HISTORY_RESTORE] Loading previous output for ${item.tool} @ ${item.target}...\n\n${item.output}`, 'info', 2);
                    scrollToLab();
                }
            };
            container.appendChild(div);
        });
    } catch (error) {
        console.error('Error fetching history:', error);
    }
}

function initMatrix() {
    const canvas = document.getElementById('matrix-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ!@#$%^&*()_+{}:|<>?';
    const charArray = chars.split('');
    
    // Layer 1: Dense, fast, small
    const fontSize1 = 12;
    const columns1 = canvas.width / fontSize1;
    const drops1 = [];
    for (let i = 0; i < columns1; i++) drops1[i] = Math.random() * -100;

    // Layer 2: Sparse, slow, large
    const fontSize2 = 20;
    const columns2 = canvas.width / fontSize2;
    const drops2 = [];
    for (let i = 0; i < columns2; i++) drops2[i] = Math.random() * -100;

    const themeColor = getComputedStyle(document.documentElement).getPropertyValue('--accent-secondary').trim() || '#39ff14';

    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw Layer 1
        ctx.font = fontSize1 + 'px monospace';
        ctx.shadowBlur = 5;
        ctx.shadowColor = themeColor;
        for (let i = 0; i < drops1.length; i++) {
            const text = charArray[Math.floor(Math.random() * charArray.length)];
            ctx.fillStyle = themeColor;
            ctx.globalAlpha = 0.3;
            ctx.fillText(text, i * fontSize1, drops1[i] * fontSize1);
            if (drops1[i] * fontSize1 > canvas.height && Math.random() > 0.975) drops1[i] = 0;
            drops1[i]++;
        }

        // Draw Layer 2
        ctx.font = fontSize2 + 'px monospace';
        ctx.shadowBlur = 10;
        ctx.shadowColor = themeColor;
        for (let i = 0; i < drops2.length; i++) {
            const text = charArray[Math.floor(Math.random() * charArray.length)];
            ctx.fillStyle = themeColor;
            ctx.globalAlpha = 0.6;
            ctx.fillText(text, i * fontSize2, drops2[i] * fontSize2);
            if (drops2[i] * fontSize2 > canvas.height && Math.random() > 0.99) drops2[i] = 0;
            drops2[i] += 0.5;
        }
        
        ctx.globalAlpha = 1.0;
        ctx.shadowBlur = 0;
    }

    if (window.matrixInterval) clearInterval(window.matrixInterval);
    window.matrixInterval = setInterval(draw, 33);

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

async function typeToTerminal(text, type = 'info', speed = 20) {
    const outputEl = document.getElementById('terminal-output');
    if (!outputEl) return;
    const div = document.createElement('div');
    if (type === 'error') div.style.color = '#ff5f56';
    outputEl.appendChild(div);

    const lines = text.split('\n');
    for (let line of lines) {
        const lineDiv = document.createElement('div');
        div.appendChild(lineDiv);
        for (let char of line) {
            lineDiv.innerHTML += char;
            outputEl.scrollTop = outputEl.scrollHeight;
            await new Promise(resolve => setTimeout(resolve, speed));
        }
    }
}

async function checkApiStatus() {
    const statusEl = document.getElementById('api-status');
    if (!statusEl) return;
    try {
        const response = await fetch(`${API_URL}/`);
        if (response.ok) {
            statusEl.innerText = 'API: ONLINE';
            statusEl.style.color = 'var(--accent-secondary)';
        } else {
            statusEl.innerText = 'API: ERROR';
            statusEl.style.color = '#ff5f56';
        }
    } catch (error) {
        statusEl.innerText = 'API: OFFLINE (Run main.py)';
        statusEl.style.color = '#ff5f56';
    }
}

async function fetchModules() {
    const container = document.getElementById('modules-container');
    const toolSelect = document.getElementById('tool-select');
    if (!container || !toolSelect) return;
    try {
        const response = await fetch(`${API_URL}/modules`);
        const modules = await response.json();
        
        container.innerHTML = '';
        toolSelect.innerHTML = '<option value="" disabled selected>Select Tool</option>';
        
        const addedTools = new Set();
        
        modules.forEach(mod => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <h3>${mod.title}</h3>
                <p>${mod.description}</p>
                <div style="margin-top: 1rem; font-size: 0.8rem; color: var(--accent-primary);">
                    Tools: ${mod.tools.join(', ')}
                </div>
            `;
            card.onclick = () => {
                toolSelect.value = mod.tools[0];
                scrollToLab();
            };
            container.appendChild(card);
            
            mod.tools.forEach(tool => {
                if (!addedTools.has(tool)) {
                    const option = document.createElement('option');
                    option.value = tool;
                    option.innerText = tool.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
                    toolSelect.appendChild(option);
                    addedTools.add(tool);
                }
            });
        });
    } catch (error) {
        console.error('Error fetching modules:', error);
        container.innerHTML = '<p style="color: #ff5f56;">Failed to load modules. Ensure the backend server is running.</p>';
    }
}

async function executeTool() {
    const toolSelect = document.getElementById('tool-select');
    const targetInput = document.getElementById('target-input');
    const outputEl = document.getElementById('terminal-output');
    const statusEl = document.getElementById('terminal-status');
    const spinner = document.getElementById('spinner');

    if (!toolSelect || !targetInput || !outputEl || !statusEl || !spinner) return;

    const tool = toolSelect.value;
    const target = targetInput.value.trim();

    if (!tool || !target) {
        appendToTerminal('[ERROR] Please select a tool and enter a target.', 'error');
        return;
    }

    statusEl.innerText = 'EXECUTING...';
    spinner.style.display = 'block';
    outputEl.innerHTML = '';
    await typeToTerminal(`[SYSTEM] CYBERHARI Secure Access Established...\n[SYSTEM] Initializing secure handshake...\n[SYSTEM] Starting ${tool} against target: ${target}...`, 'info', 10);

    try {
        const response = await fetch(`${API_URL}/run-tool`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ tool, target })
        });

        const data = await response.json();
        
        if (response.ok) {
            await typeToTerminal(data.output, 'info', 5);
            statusEl.innerText = 'SUCCESS';
            fetchLabHistory();
        } else {
            await typeToTerminal(`[ERROR] ${data.detail || 'Execution failed.'}`, 'error');
            statusEl.innerText = 'FAILED';
        }
    } catch (error) {
        await typeToTerminal(`[ERROR] Network error: Could not reach backend.`, 'error');
        statusEl.innerText = 'OFFLINE';
    } finally {
        spinner.style.display = 'none';
    }
}

function appendToTerminal(text, type = 'info') {
    const outputEl = document.getElementById('terminal-output');
    if (!outputEl) return;
    const div = document.createElement('div');
    if (type === 'error') div.style.color = '#ff5f56';
    div.innerText = text;
    outputEl.appendChild(div);
    outputEl.scrollTop = outputEl.scrollHeight;
}

function scrollToLab() {
    const lab = document.getElementById('lab');
    if (lab) lab.scrollIntoView({ behavior: 'smooth' });
}
