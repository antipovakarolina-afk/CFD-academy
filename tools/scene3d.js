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

// ---------- лес, великан, девочка, птичка, светлячки ----------
function rng(seed) { let s = seed; return () => (s = (s * 9301 + 49297) % 233280) / 233280; }
Object.assign(Models, {
  forest(night = false, seed = 3) {
    const g = new THREE.Group(), r = rng(seed); g.userData.noPop = true;
    const ground = new THREE.Mesh(new THREE.PlaneGeometry(80, 80), M(night ? '#232a3a' : '#5d7a52', {roughness: 1}));
    ground.rotation.x = -Math.PI / 2; ground.position.set(0, -1.66, -10); ground.receiveShadow = true; g.add(ground);
    const trunk = M(night ? '#3a3f58' : '#7d8f84', {roughness: .9});
    for (let i = 0; i < 26; i++) {
      const z = -2.5 - r() * 16, x = (r() - 0.5) * (8 + -z * 1.1), rad = 0.12 + r() * 0.22;
      if (Math.abs(x) < 1.6 && z > -6) continue;
      const t = mesh(new THREE.CylinderGeometry(rad * 0.7, rad, 16, 10), trunk); t.position.set(x, 6, z); t.rotation.z = (r() - 0.5) * 0.08; g.add(t);
      for (let b = 0; b < 2; b++) { const br = mesh(new THREE.CylinderGeometry(0.03, 0.06, 2.2, 6), trunk); br.position.set(x + (r() - .5), 2.5 + r() * 4, z);
        br.rotation.z = (r() > .5 ? 1 : -1) * (0.6 + r() * 0.5); g.add(br); }
    }
    const rockM = M(night ? '#3b4256' : '#5f6a5c', {roughness: .95}), mossM = M(night ? '#3d5a4a' : '#6f9a4f', {roughness: 1});
    for (let i = 0; i < 12; i++) {
      const side = i % 2 ? 1 : -1, x = side * (1.6 + r() * 2.2), z = -0.5 - r() * 4, sc = 0.4 + r() * 0.6;
      const rock = mesh(new THREE.IcosahedronGeometry(1, 1), rockM); rock.scale.set(sc * 1.3, sc * 0.8, sc); rock.position.set(x, -1.66 + sc * 0.4, z); g.add(rock);
      const moss = mesh(new THREE.SphereGeometry(1, 16, 12), mossM); moss.scale.set(sc * 1.15, sc * 0.35, sc * 0.9); moss.position.set(x, -1.66 + sc * 0.95, z); g.add(moss);
    }
    return g;
  },
  giant(withGirl = false, mood = 'smile') {
    const g = new THREE.Group(), r = rng(11);
    const furM = M('#4f8a44', {roughness: 1});
    const body = mesh(new THREE.SphereGeometry(1.5, 32, 24), furM); body.scale.set(1.15, 1.2, 0.95); body.position.set(0, 1.55, 0); g.add(body);
    [[-0.68, 0.45, 0.75], [0.68, 0.45, 0.75]].forEach(p => { const k = mesh(new THREE.SphereGeometry(0.62, 24, 18), M('#5a9a4a', {roughness: 1})); k.scale.set(1, 0.85, 1.1); k.position.set(...p); g.add(k); });
    [[-1.5, 1.1, 0.35, 0.5], [1.5, 1.1, 0.35, -0.5]].forEach(([x, y, z, rz]) => { const a = mesh(new THREE.SphereGeometry(0.4, 18, 14), furM); a.scale.set(0.8, 1.9, 0.8); a.position.set(x, y, z); a.rotation.z = rz; g.add(a); });
    const face = mesh(new THREE.SphereGeometry(0.72, 32, 24), M('#77ad5a', {roughness: .95})); face.scale.set(1.05, 0.78, 0.45); face.position.set(0, 2.2, 1.1); g.add(face);
    const eyeM = M('#151515', {roughness: .2});
    [[-0.26, 2.36], [0.26, 2.36]].forEach(([x, y]) => { const e = mesh(new THREE.SphereGeometry(0.085, 16, 12), eyeM); e.position.set(x, y, 1.38); g.add(e);
      const h = mesh(new THREE.SphereGeometry(0.025, 8, 8), M('#fff', {emissive: '#fff', emissiveIntensity: .5})); h.position.set(x + 0.03, y + 0.04, 1.45); g.add(h); });
    const smile = mesh(new THREE.TorusGeometry(mood === 'big' ? 0.3 : 0.24, 0.035, 8, 24, Math.PI), M('#2f5f2f')); smile.rotation.z = Math.PI; smile.position.set(0, 2.12, 1.38); g.add(smile);
    [[-0.48, 2.1], [0.48, 2.1]].forEach(([x, y]) => { const c = mesh(new THREE.SphereGeometry(0.11, 12, 10), M('#ff9fb3', {transparent: true, opacity: .45})); c.scale.z = .3; c.position.set(x, y, 1.33); g.add(c); });
    // шерсть: тысячи «прядей»
    const N = 2600, geo = new THREE.ConeGeometry(0.07, 0.34, 5); geo.translate(0, 0.17, 0);
    const fur = new THREE.InstancedMesh(geo, M('#ffffff', {roughness: 1}), N); fur.castShadow = true;
    const cols = ['#3f7a3a', '#5a9a4a', '#2f5f2f', '#7cae5a', '#4c8a3e'].map(c => new THREE.Color(c));
    const dummy = new THREE.Object3D(), up = new THREE.Vector3(0, 1, 0); let k = 0;
    while (k < N) {
      const th = r() * Math.PI * 2, ph = Math.acos(2 * r() - 1);
      const n = new THREE.Vector3(Math.sin(ph) * Math.cos(th), Math.cos(ph), Math.sin(ph) * Math.sin(th));
      const p = new THREE.Vector3(n.x * 1.5 * 1.15, n.y * 1.5 * 1.2 + 1.55, n.z * 1.5 * 0.95);
      if (p.z > 0.55 && p.y > 1.6 && p.y < 2.75 && Math.abs(p.x) < 0.85) continue;   // лицо без шерсти
      if (p.y < 0.2) continue;
      const dir = n.clone().multiplyScalar(0.55).add(new THREE.Vector3((r() - .5) * .35, n.y > .75 ? 0.5 : -0.75, (r() - .5) * .35)).normalize();
      dummy.position.copy(p); dummy.quaternion.setFromUnitVectors(up, dir);
      const sc = 0.6 + r() * (n.y > .8 ? 1.2 : 0.6); dummy.scale.set(1, sc, 1); dummy.updateMatrix();
      fur.setMatrixAt(k, dummy.matrix); fur.setColorAt(k, cols[Math.floor(r() * cols.length)]); k++;
    }
    g.add(fur);
    if (withGirl) { const girl = Models.girl(); girl.position.set(0.78, 0.82, 1.5); girl.rotation.y = -0.2; girl.scale.setScalar(2.3); g.add(girl); }
    return g;
  },
  girl() {
    const g = new THREE.Group();
    const dress = mesh(new THREE.ConeGeometry(0.16, 0.34, 18), M('#d9c2a2')); dress.position.y = 0.17; g.add(dress);
    const collar = mesh(new THREE.TorusGeometry(0.07, 0.02, 8, 16), M('#5a3a2a')); collar.rotation.x = Math.PI / 2; collar.position.y = 0.33; g.add(collar);
    const head = mesh(new THREE.SphereGeometry(0.1, 20, 16), M('#f7dccb')); head.position.y = 0.44; g.add(head);
    const hair = mesh(new THREE.SphereGeometry(0.108, 20, 16, 0, Math.PI * 2, 0, Math.PI * 0.55), M('#2b1d1a')); hair.position.y = 0.45; hair.rotation.x = -0.35; g.add(hair);
    const tail = mesh(new THREE.SphereGeometry(0.06, 12, 10), M('#2b1d1a')); tail.scale.set(0.8, 1.5, 0.8); tail.position.set(0, 0.46, -0.13); g.add(tail);
    const bun = mesh(new THREE.SphereGeometry(0.045, 10, 8), M('#2b1d1a')); bun.position.set(0, 0.54, -0.07); g.add(bun);
    const book = mesh(new THREE.BoxGeometry(0.2, 0.14, 0.02), M('#fff8ee')); book.position.set(0, 0.27, 0.15); book.rotation.x = -0.7; g.add(book);
    const cover = mesh(new THREE.BoxGeometry(0.21, 0.145, 0.01), M('#9b6ef3')); cover.position.set(0, 0.265, 0.14); cover.rotation.x = -0.7; g.add(cover);
    return g;
  },
  bird(color = '#a98bf0') {
    const g = new THREE.Group();
    const b = mesh(new THREE.SphereGeometry(0.22, 20, 16), M(color)); b.scale.set(1.25, 1, 1); g.add(b);
    const h = mesh(new THREE.SphereGeometry(0.14, 18, 14), M(color)); h.position.set(0.2, 0.17, 0); g.add(h);
    const beak = mesh(new THREE.ConeGeometry(0.04, 0.12, 8), M('#ffb347')); beak.rotation.z = -Math.PI / 2; beak.position.set(0.37, 0.16, 0); g.add(beak);
    const e = mesh(new THREE.SphereGeometry(0.025, 8, 8), M('#111')); e.position.set(0.27, 0.21, 0.1); g.add(e);
    const w = mesh(new THREE.SphereGeometry(0.16, 14, 10), M('#8a6ae0')); w.scale.set(1.1, 0.5, 0.3); w.position.set(-0.03, 0.04, 0.17); w.rotation.z = 0.4; w.userData.wing = true; g.add(w);
    const t = mesh(new THREE.ConeGeometry(0.07, 0.25, 8), M('#8a6ae0')); t.rotation.z = Math.PI / 2 + 0.4; t.position.set(-0.32, 0.06, 0); g.add(t);
    return g;
  },
  fireflies(n = 30, color = '#c9a7ff', seed = 4, spread = 3.2) {
    const g = new THREE.Group(), r = rng(seed); g.userData.noPop = true;
    for (let i = 0; i < n; i++) {
      const f = new THREE.Mesh(new THREE.SphereGeometry(0.035 + r() * 0.03, 8, 8), new THREE.MeshBasicMaterial({color}));
      const halo = new THREE.Mesh(new THREE.SphereGeometry(0.12, 8, 8), new THREE.MeshBasicMaterial({color, transparent: true, opacity: 0.18}));
      f.add(halo); f.position.set((r() - .5) * spread * 1.4, (r() - .3) * spread, (r() - .5) * 2.5);
      f.userData.float = {x: f.position.x, y: f.position.y, p: r() * 6.28, a: 0.15 + r() * 0.2}; g.add(f);
    }
    return g;
  },
});

// ---------- детский 3D (глянец, как в мультиках) ----------
const GLOSS = (c, o = {}) => new THREE.MeshPhysicalMaterial(Object.assign({color: c, roughness: 0.28, metalness: 0, clearcoat: 1, clearcoatRoughness: 0.15}, o));
function glow(color, r = 1, op = 0.25) { const m = new THREE.Mesh(new THREE.SphereGeometry(r, 24, 16), new THREE.MeshBasicMaterial({color, transparent: true, opacity: op, depthWrite: false})); m.castShadow = false; return m; }
function cuteEyes(g, x, y, z, s = 1, iris = '#3fa9f5') {
  [-1, 1].forEach(sd => {
    const w = mesh(new THREE.SphereGeometry(0.15 * s, 24, 16), GLOSS('#ffffff')); w.scale.set(0.85, 1.1, 0.55); w.position.set(x + sd * 0.19 * s, y, z); g.add(w);
    const ir = mesh(new THREE.SphereGeometry(0.09 * s, 20, 14), GLOSS(iris)); ir.scale.set(1, 1.1, 0.5); ir.position.set(x + sd * 0.19 * s, y - 0.01 * s, z + 0.07 * s); g.add(ir);
    const p = mesh(new THREE.SphereGeometry(0.05 * s, 16, 12), GLOSS('#111')); p.scale.z = 0.5; p.position.set(x + sd * 0.19 * s, y - 0.01 * s, z + 0.1 * s); g.add(p);
    const h = mesh(new THREE.SphereGeometry(0.025 * s, 10, 8), new THREE.MeshBasicMaterial({color: '#fff'})); h.position.set(x + sd * 0.19 * s + 0.03 * s, y + 0.04 * s, z + 0.12 * s); g.add(h);
  });
}
Object.assign(Models, {
  glossyStar(color = '#ffd43b') {
    const s = new THREE.Shape();
    for (let i = 0; i < 10; i++) { const r = i % 2 ? 0.27 : 0.62, a = i * Math.PI / 5; const x = r * Math.sin(a), y = r * Math.cos(a); i ? s.lineTo(x, y) : s.moveTo(x, y); }
    const geo = new THREE.ExtrudeGeometry(s, {depth: 0.14, bevelEnabled: true, bevelSize: 0.12, bevelThickness: 0.14, bevelSegments: 8, curveSegments: 12}); geo.center();
    const g = new THREE.Group();
    g.add(mesh(geo, GLOSS(color, {emissive: '#ffb703', emissiveIntensity: 0.35})));
    g.add(glow('#ffe066', 0.78, 0.07));
    cuteEyes(g, 0, 0.06, 0.22, 0.9);
    const sm = mesh(new THREE.TorusGeometry(0.1, 0.022, 8, 20, Math.PI), GLOSS('#7a3b00')); sm.rotation.z = Math.PI; sm.position.set(0, -0.13, 0.27); g.add(sm);
    [-0.3, 0.3].forEach(x => { const c = mesh(new THREE.SphereGeometry(0.06, 12, 10), new THREE.MeshBasicMaterial({color: '#ff8fab', transparent: true, opacity: .6})); c.scale.z = .3; c.position.set(x, -0.08, 0.25); g.add(c); });
    return g;
  },
  bear(color = '#c68b59') {
    const g = new THREE.Group(), fur = GLOSS(color, {roughness: .6, clearcoat: .3}), light = GLOSS('#f1d3b3', {roughness: .6, clearcoat: .3});
    const body = mesh(new THREE.SphereGeometry(0.45, 32, 24), fur); body.scale.set(1, 1.1, 0.9); body.position.y = 0.45; g.add(body);
    const belly = mesh(new THREE.SphereGeometry(0.3, 24, 16), light); belly.scale.set(1, 1.1, 0.5); belly.position.set(0, 0.42, 0.3); g.add(belly);
    const head = mesh(new THREE.SphereGeometry(0.42, 32, 24), fur); head.position.y = 1.15; g.add(head);
    [-1, 1].forEach(sd => { const e = mesh(new THREE.SphereGeometry(0.15, 20, 16), fur); e.position.set(sd * 0.33, 1.48, -0.02); g.add(e);
      const ei = mesh(new THREE.SphereGeometry(0.08, 16, 12), light); ei.position.set(sd * 0.33, 1.48, 0.08); g.add(ei);
      const arm = mesh(new THREE.SphereGeometry(0.15, 16, 12), fur); arm.scale.set(1, 1.6, 1); arm.position.set(sd * 0.45, 0.55, 0.15); arm.rotation.z = sd * 0.5; g.add(arm);
      const leg = mesh(new THREE.SphereGeometry(0.17, 16, 12), fur); leg.scale.set(1, 0.8, 1.3); leg.position.set(sd * 0.22, 0.08, 0.2); g.add(leg); });
    const muzzle = mesh(new THREE.SphereGeometry(0.17, 20, 16), light); muzzle.scale.set(1.2, 0.85, 0.8); muzzle.position.set(0, 1.04, 0.36); g.add(muzzle);
    const nose = mesh(new THREE.SphereGeometry(0.06, 14, 10), GLOSS('#3b2416')); nose.scale.set(1.3, 0.9, 0.8); nose.position.set(0, 1.1, 0.5); g.add(nose);
    cuteEyes(g, 0, 1.24, 0.33, 0.75, '#6b3e1f');
    return g;
  },
  room(night = true) {
    const g = new THREE.Group(); g.userData.noPop = true;
    const wall = new THREE.Mesh(new THREE.PlaneGeometry(14, 12), M('#5b4bb0', {roughness: .9})); wall.position.set(0, 2, -3); wall.receiveShadow = true; g.add(wall);
    const floor = new THREE.Mesh(new THREE.PlaneGeometry(14, 8), M('#7a68cf', {roughness: .9})); floor.rotation.x = -Math.PI / 2; floor.position.set(0, -1.7, 0); floor.receiveShadow = true; g.add(floor);
    const rug = mesh(new THREE.CylinderGeometry(1.6, 1.6, 0.04, 40), M('#ff9ecd')); rug.position.set(0.3, -1.68, 0.4); g.add(rug);
    const win = mesh(rbox(1.8, 2.0, 0.15, 0.2), GLOSS('#f5e6ff')); win.position.set(-1.3, 2.3, -2.9); g.add(win);
    const pane = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 1.7), new THREE.MeshBasicMaterial({color: '#1d2a6b'})); pane.position.set(-1.3, 2.3, -2.8); g.add(pane);
    const mn = Models.moon('#fff1a8'); mn.scale.setScalar(0.45); mn.position.set(-1.1, 2.5, -2.75); g.add(mn);
    const bed = new THREE.Group();
    const frame = mesh(rbox(2.6, 0.5, 1.4, 0.12), GLOSS('#c77dff')); frame.position.y = -1.3; bed.add(frame);
    const head = mesh(rbox(0.25, 1.4, 1.4, 0.12), GLOSS('#b15cff')); head.position.set(-1.3, -0.95, 0); bed.add(head);
    const blanket = mesh(rbox(1.9, 0.25, 1.45, 0.12), GLOSS('#ffd6ec')); blanket.position.set(0.3, -0.95, 0); bed.add(blanket);
    const pillow = mesh(rbox(0.6, 0.25, 0.9, 0.12), GLOSS('#ffffff')); pillow.position.set(-0.9, -0.9, 0); bed.add(pillow);
    bed.position.set(1.4, 0, -1.6); g.add(bed);
    const lamp = new THREE.PointLight('#ffd27a', 1.4, 10); lamp.position.set(0, 1.5, 2.5); g.add(lamp);
    return g;
  },
  sparkles(n = 25, seed = 5, spread = 3.4, color = '#fff3b0') {
    const g = new THREE.Group(), r = rng(seed); g.userData.noPop = true;
    for (let i = 0; i < n; i++) {
      const st = Models.star(color, 1.2); st.scale.setScalar(0.08 + r() * 0.12);
      st.position.set((r() - .5) * spread * 1.2, (r() - .35) * spread * 1.3, (r() - .5) * 1.5);
      st.userData.float = {x: st.position.x, y: st.position.y, p: r() * 6.28, a: 0.06 + r() * 0.1}; g.add(st);
    }
    return g;
  },
  earth3d() {
    const g = new THREE.Group(), r = rng(9);
    g.add(mesh(new THREE.SphereGeometry(1, 48, 32), GLOSS('#3fa9f5')));
    for (let i = 0; i < 9; i++) { const th = r() * 6.28, ph = 0.5 + r() * 2.1; const c = mesh(new THREE.SphereGeometry(0.28 + r() * 0.2, 16, 12), GLOSS('#5fd068'));
      c.scale.set(1, 0.6, 0.35); c.position.set(Math.sin(ph) * Math.cos(th) * 0.93, Math.cos(ph) * 0.93, Math.sin(ph) * Math.sin(th) * 0.93); c.lookAt(0, 0, 0); g.add(c); }
    g.add(glow('#8fd3ff', 1.08, 0.08)); g.userData.spinY = 0.5;
    return g;
  },
  crystal() {
    const g = new THREE.Group();
    const geo = new THREE.OctahedronGeometry(0.8, 0); geo.scale(1, 1.25, 1);
    g.add(mesh(geo, new THREE.MeshPhysicalMaterial({color: '#b8ecff', roughness: 0.05, metalness: 0.1, clearcoat: 1, flatShading: true, emissive: '#5ac8fa', emissiveIntensity: 0.25})));
    g.add(glow('#bdf0ff', 1.05, 0.07));
    return g;
  },
});
