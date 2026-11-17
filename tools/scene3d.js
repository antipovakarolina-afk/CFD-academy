// 3D-модели в «игрушечном / пластилиновом» стиле для рилсов (three.js r150).
// Каждая функция возвращает THREE.Group. Единицы: ~1 = 100 px в кадре.
const M = (c, o = {}) => new THREE.MeshStandardMaterial(Object.assign({color: c, roughness: 0.55, metalness: 0}, o));
const GOLD = () => M('#f2c14e', {metalness: 0.55, roughness: 0.3});
function mesh(geo, mat) { const m = new THREE.Mesh(geo, mat); m.castShadow = true; m.receiveShadow = true; return m; }
function grp(...a) { const g = new THREE.Group(); a.forEach(x => g.add(x)); return g; }
function at(o, x, y, z) { o.position.set(x, y, z || 0); return o; }
function rot(o, x, y, z) { o.rotation.set(x || 0, y || 0, z || 0); return o; }
function rbox(w, h, d, r) { // скруглённая коробка
  const s = new THREE.Shape(); const x = -w / 2, y = -h / 2;
  s.moveTo(x + r, y); s.lineTo(x + w - r, y); s.quadraticCurveTo(x + w, y, x + w, y + r); s.lineTo(x + w, y + h - r);
  s.quadraticCurveTo(x + w, y + h, x + w - r, y + h); s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y);
  const g = new THREE.ExtrudeGeometry(s, {depth: d - 2 * Math.min(r, d / 3), bevelEnabled: true, bevelSize: Math.min(r, d / 3), bevelThickness: Math.min(r, d / 3), bevelSegments: 4, curveSegments: 8});
  g.center(); return g;
}
function canvasTex(w, h, draw) {
  const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); t.anisotropy = 4; t.encoding = THREE.sRGBEncoding; return t;
}

const Models = {
  gift(color = '#e63946', ribbon = '#ffd23f') {
    const b = mesh(rbox(1, 0.8, 1, 0.06), M(color)); at(b, 0, 0.4);
    const lid = mesh(rbox(1.12, 0.22, 1.12, 0.06), M(color)); at(lid, 0, 0.88);
    const r1 = mesh(new THREE.BoxGeometry(0.18, 1.04, 1.14), M(ribbon)); at(r1, 0, 0.5);
    const r2 = mesh(new THREE.BoxGeometry(1.14, 1.04, 0.18), M(ribbon)); at(r2, 0, 0.5);
    const t1 = mesh(new THREE.TorusGeometry(0.2, 0.07, 12, 24), M(ribbon)); rot(at(t1, -0.18, 1.12), 0, 0, 0.6);
    const t2 = mesh(new THREE.TorusGeometry(0.2, 0.07, 12, 24), M(ribbon)); rot(at(t2, 0.18, 1.12), 0, 0, -0.6);
    return grp(b, lid, r1, r2, t1, t2);
  },
  candle(h = 1.0) {
    const body = mesh(new THREE.CylinderGeometry(0.17, 0.18, h, 24), M('#fffaf0')); at(body, 0, h / 2);
    const wick = mesh(new THREE.CylinderGeometry(0.015, 0.015, 0.1, 6), M('#333')); at(wick, 0, h + 0.05);
    const fl = mesh(new THREE.SphereGeometry(0.09, 16, 16), M('#ffcf3a', {emissive: '#ff9a00', emissiveIntensity: 1.2}));
    fl.scale.set(1, 1.8, 1); at(fl, 0, h + 0.2); fl.castShadow = false; fl.userData.flame = true;
    const plate = mesh(new THREE.CylinderGeometry(0.3, 0.3, 0.05, 24), M('#d9b48f')); at(plate, 0, 0.02);
    return grp(plate, body, wick, fl);
  },
  figurine(color = '#c98b5a') {
    const body = mesh(new THREE.CylinderGeometry(0.18, 0.32, 0.7, 20), M(color)); at(body, 0, 0.35);
    const head = mesh(new THREE.SphereGeometry(0.22, 24, 24), M(color)); at(head, 0, 0.92);
    const e1 = mesh(new THREE.SphereGeometry(0.03, 8, 8), M('#222')); at(e1, -0.08, 0.95, 0.2);
    const e2 = mesh(new THREE.SphereGeometry(0.03, 8, 8), M('#222')); at(e2, 0.08, 0.95, 0.2);
    return grp(body, head, e1, e2);
  },
  star(color = '#ffd23f', glow = 0.4) {
    const s = new THREE.Shape();
    for (let i = 0; i < 10; i++) { const r = i % 2 ? 0.22 : 0.55, a = i * Math.PI / 5 - Math.PI / 2; const x = r * Math.cos(a), y = -r * Math.sin(a); i ? s.lineTo(x, y) : s.moveTo(x, y); }
    const g = new THREE.ExtrudeGeometry(s, {depth: 0.12, bevelEnabled: true, bevelSize: 0.05, bevelThickness: 0.05, bevelSegments: 3}); g.center();
    return grp(mesh(g, M(color, {emissive: color, emissiveIntensity: glow})));
  },
  coin() { const c = mesh(new THREE.CylinderGeometry(0.28, 0.28, 0.07, 32), GOLD()); rot(c, Math.PI / 2, 0, 0); return grp(c); },
  bag(color = '#c9a659') {
    const b = mesh(new THREE.SphereGeometry(0.6, 32, 32), M(color)); b.scale.set(1, 0.9, 0.9); at(b, 0, 0.55);
    const neck = mesh(new THREE.CylinderGeometry(0.16, 0.3, 0.3, 20), M(color)); at(neck, 0, 1.1);
    const top = mesh(new THREE.ConeGeometry(0.25, 0.22, 20), M(color)); rot(at(top, 0, 1.33), Math.PI, 0, 0);
    const tie = mesh(new THREE.TorusGeometry(0.18, 0.04, 10, 24), M('#8a6d2b')); rot(at(tie, 0, 1.18), Math.PI / 2, 0, 0);
    const g = grp(b, neck, top, tie);
    [[-0.7, 0.07, 0.4], [0.75, 0.07, 0.3], [0.5, 0.07, 0.7]].forEach(([x, y, z]) => { const c = mesh(new THREE.CylinderGeometry(0.22, 0.22, 0.06, 28), GOLD()); at(c, x, y, z); g.add(c); });
    return g;
  },
  fireplace() {
    const body = mesh(new THREE.BoxGeometry(2.4, 1.6, 0.6), M('#c97b4a')); at(body, 0, 0.8);
    const mantel = mesh(rbox(2.8, 0.22, 0.85, 0.05), M('#8a4a2a')); at(mantel, 0, 1.7);
    const hole = mesh(new THREE.BoxGeometry(1.2, 0.95, 0.4), M('#2b2230')); at(hole, 0, 0.52, 0.15);
    const g = grp(body, mantel, hole);
    [[-0.2, 0.45, '#ff8c2b', 0.5], [0.15, 0.4, '#ffb347', 0.4], [0, 0.35, '#ffd23f', 0.3]].forEach(([x, h, c, r]) => {
      const f = mesh(new THREE.ConeGeometry(0.2 * r / 0.3, h, 16), M(c, {emissive: c, emissiveIntensity: 1})); f.castShadow = false; f.userData.flame = true;
      at(f, x, 0.08 + h / 2, 0.3); g.add(f);
    });
    for (let i = 0; i < 4; i++) { const l = mesh(new THREE.BoxGeometry(2.42, 0.02, 0.62), M('#a8623a')); at(l, 0, 0.35 + i * 0.35); g.add(l); }
    return g;
  },
  stocking(color = '#e63946') {
    const leg = mesh(rbox(0.42, 0.8, 0.3, 0.12), M(color)); at(leg, 0, 0);
    const foot = mesh(new THREE.SphereGeometry(0.27, 24, 24), M(color)); foot.scale.set(1.4, 0.85, 0.9); at(foot, 0.16, -0.42);
    const cuff = mesh(rbox(0.5, 0.2, 0.36, 0.08), M('#ffffff')); at(cuff, 0, 0.47);
    return grp(leg, foot, cuff);
  },
  calendar(month = 'DEC', day = '25', color = '#e63946') {
    const tex = canvasTex(512, 600, (c, w, h) => {
      c.fillStyle = '#fff'; c.fillRect(0, 0, w, h); c.fillStyle = color; c.fillRect(0, 0, w, 170);
      c.fillStyle = '#fff'; c.font = 'bold 110px Hand'; c.textAlign = 'center'; c.fillText(month, w / 2, 130);
      c.fillStyle = '#222'; c.font = 'bold 330px Hand'; c.fillText(day, w / 2, 500);
    });
    const page = mesh(rbox(1.5, 1.75, 0.18, 0.08), [M('#fff')]);
    const front = mesh(new THREE.PlaneGeometry(1.42, 1.66), new THREE.MeshStandardMaterial({map: tex, roughness: 0.7}));
    at(front, 0, 0, 0.1);
    const r1 = mesh(new THREE.TorusGeometry(0.1, 0.03, 8, 20), M('#888', {metalness: .6})); rot(at(r1, -0.4, 0.9, 0), 0, Math.PI / 2, 0);
    const r2 = r1.clone(); at(r2, 0.4, 0.9, 0);
    return grp(page, front, r1, r2);
  },
  scroll() {
    const tex = canvasTex(400, 460, (c, w, h) => {
      c.fillStyle = '#fff4d6'; c.fillRect(0, 0, w, h); c.strokeStyle = '#a8946a'; c.lineWidth = 10; c.lineCap = 'round';
      for (let i = 0; i < 6; i++) { c.beginPath(); c.moveTo(50, 70 + i * 62); c.lineTo(w - 50 - (i % 2) * 80, 70 + i * 62); c.stroke(); }
    });
    const sheet = mesh(new THREE.PlaneGeometry(1.4, 1.6), new THREE.MeshStandardMaterial({map: tex, side: THREE.DoubleSide, roughness: .8}));
    const c1 = mesh(new THREE.CylinderGeometry(0.12, 0.12, 1.6, 24), M('#e8d2a8')); rot(at(c1, 0, 0.82), 0, 0, Math.PI / 2);
    const c2 = c1.clone(); at(c2, 0, -0.82);
    return grp(sheet, c1, c2);
  },
  moon(color = '#ffd23f') {
    const s = new THREE.Shape(); s.absarc(0, 0, 0.6, Math.PI * 0.35, Math.PI * 1.65, false);
    s.absarc(0.28, 0, 0.5, Math.PI * 1.55, Math.PI * 0.45, true);
    const g = new THREE.ExtrudeGeometry(s, {depth: 0.2, bevelEnabled: true, bevelSize: 0.05, bevelThickness: 0.05, bevelSegments: 4, curveSegments: 32}); g.center();
    return grp(mesh(g, M(color, {emissive: color, emissiveIntensity: 0.35})));
  },
  paperRoll(color = '#e63946', dots = '#ffd23f') {
    const tex = canvasTex(512, 256, (c, w, h) => { c.fillStyle = color; c.fillRect(0, 0, w, h); c.fillStyle = dots;
      for (let y = 20; y < h; y += 44) for (let x = 20 + (y / 44 % 2) * 22; x < w; x += 44) { c.beginPath(); c.arc(x, y, 9, 0, 7); c.fill(); } });
    tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
    const roll = mesh(new THREE.CylinderGeometry(0.35, 0.35, 1.8, 40), new THREE.MeshStandardMaterial({map: tex, roughness: .5}));
    rot(roll, 0, 0, Math.PI / 2); at(roll, 0, 0.35);
    const core = mesh(new THREE.CylinderGeometry(0.12, 0.12, 1.82, 20), M('#fff')); rot(at(core, 0, 0.35), 0, 0, Math.PI / 2);
    const t2 = tex.clone(); t2.needsUpdate = true;
    const sheet = mesh(new THREE.BoxGeometry(1.8, 0.02, 1.2), new THREE.MeshStandardMaterial({map: t2, roughness: .5})); at(sheet, 0, 0.01, 0.75);
    return grp(roll, core, sheet);
  },
  heart(color = '#e0457b') {
    const s = new THREE.Shape(); s.moveTo(0, -0.55);
    s.bezierCurveTo(-0.95, 0.05, -0.55, 0.8, 0, 0.35); s.bezierCurveTo(0.55, 0.8, 0.95, 0.05, 0, -0.55);
    const g = new THREE.ExtrudeGeometry(s, {depth: 0.25, bevelEnabled: true, bevelSize: 0.1, bevelThickness: 0.1, bevelSegments: 6, curveSegments: 32}); g.center();
    return grp(mesh(g, M(color, {roughness: .35})));
  },
  brain(color = '#ff9fb3') {
    const g = new THREE.Group();
    [[-0.35, 0.1, 0, 0.45], [0.35, 0.1, 0, 0.45], [-0.25, 0.4, 0.05, 0.38], [0.25, 0.4, 0.05, 0.38], [0, -0.15, 0, 0.4], [-0.5, -0.15, 0, 0.32], [0.5, -0.15, 0, 0.32]]
      .forEach(([x, y, z, r]) => { const s = mesh(new THREE.SphereGeometry(r, 24, 24), M(color, {roughness: .45})); at(s, x, y, z); g.add(s); });
    return g;
  },
  phone(query = '') {
    const tex = canvasTex(500, 900, (c, w, h) => {
      c.fillStyle = '#fff'; c.fillRect(0, 0, w, h);
      const cols = ['#4285F4', '#EA4335', '#FBBC05', '#4285F4', '#34A853', '#EA4335']; c.font = 'bold 130px Hand'; let x = 70;
      'google'.split('').forEach((ch, i) => { c.fillStyle = cols[i]; c.fillText(ch, x, 330); x += c.measureText(ch).width; });
      c.strokeStyle = '#444'; c.lineWidth = 6; c.beginPath(); c.roundRect(40, 400, w - 80, 100, 50); c.stroke();
      c.fillStyle = '#333'; c.font = `bold ${Math.min(48, 760 / Math.max(1, query.length))}px Hand`; c.fillText(query, 75, 465);
      c.strokeStyle = '#ccd'; c.lineWidth = 10; [580, 640, 700].forEach((y, i) => { c.beginPath(); c.moveTo(60, y); c.lineTo(w - 80 - i * 50, y); c.stroke(); });
    });
    const body = mesh(rbox(1.5, 2.6, 0.18, 0.2), M('#2b2d33'));
    const scr = new THREE.Mesh(new THREE.PlaneGeometry(1.36, 2.4), new THREE.MeshBasicMaterial({map: tex})); at(scr, 0, 0, 0.1);
    return grp(body, scr);
  },
  snow(n = 40, seed = 1) {
    const g = new THREE.Group(); let r = seed;
    const rnd = () => (r = (r * 9301 + 49297) % 233280) / 233280;
    for (let i = 0; i < n; i++) { const s = new THREE.Mesh(new THREE.SphereGeometry(0.03 + rnd() * 0.04, 8, 8), M('#ffffff', {emissive: '#fff', emissiveIntensity: .5}));
      s.position.set((rnd() - 0.5) * 4, (rnd() - 0.5) * 5, (rnd() - 0.5) * 2); s.userData.snow = 0.2 + rnd() * 0.3; g.add(s); }
    g.userData.noPop = true; return g;
  },
};
