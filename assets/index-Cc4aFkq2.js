var z=Object.defineProperty;var V=(t,e,s)=>e in t?z(t,e,{enumerable:!0,configurable:!0,writable:!0,value:s}):t[e]=s;var _=(t,e,s)=>V(t,typeof e!="symbol"?e+"":e,s);(function(){const e=document.createElement("link").relList;if(e&&e.supports&&e.supports("modulepreload"))return;for(const n of document.querySelectorAll('link[rel="modulepreload"]'))o(n);new MutationObserver(n=>{for(const i of n)if(i.type==="childList")for(const a of i.addedNodes)a.tagName==="LINK"&&a.rel==="modulepreload"&&o(a)}).observe(document,{childList:!0,subtree:!0});function s(n){const i={};return n.integrity&&(i.integrity=n.integrity),n.referrerPolicy&&(i.referrerPolicy=n.referrerPolicy),n.crossOrigin==="use-credentials"?i.credentials="include":n.crossOrigin==="anonymous"?i.credentials="omit":i.credentials="same-origin",i}function o(n){if(n.ep)return;n.ep=!0;const i=s(n);fetch(n.href,i)}})();const P=3,B=128,A={"Block (1x1)":{id:0,width:1*B,height:1*B},"Block (2x2)":{id:63,width:2*B,height:2*B},"Block (1x4)":{id:43,width:1*B,height:4*B},"Block (4x1)":{id:42,width:4*B,height:1*B}},$="Wall Tool",Z=["Block (1x1)","Block (2x2)","Block (1x4)","Block (4x1)","Wall Tool"];class U{constructor(e,s,o=null){_(this,"type");_(this,"sound");_(this,"table");this.type=e,this.sound=s,this.table=o?[...o]:[]}get(e){return this.table[e]}set(e,s){this.table[e]=s}toString(){return`Type: ${this.type}
 Sound: ${this.sound}
 Table: ${JSON.stringify(this.table)}
`}}function k(t){const e=t.Config;return[Number(e.MapWidth),Number(e.MapHeight)]}function q(t,e){const s=[],o=[];for(const[n,i]of Object.entries(t))n!=="Config"&&e.includes(i.Name)?s.push(i):o.push(i);return[s,o]}function G(t,e){const s=Array(t).fill(0);return Array(e).fill(null).map(()=>[...s])}function K(t,e,s){const o=t.X,n=t.Y;if(t.Name===e)return[Number(o),Number(n),Number(t.ObjWallWidth),Number(t.ObjWallHeight)];const i=s[t.Name];return[Number(o),Number(n),i.width,i.height]}function Q(t,e){for(let s=0;s<t.length;s++){const o=t[s];if(o.type===e.ObjType&&o.sound===e.ObjSound)return s}return-1}function J(t,e){return t%e===0}function tt(t,e,s,o,n,i=1){const a=Math.floor(t/i),l=Math.floor(e/i),f=G(a,l),h=[];function u(r,c){return r>=0&&r<a&&c>=0&&c<l}function p(r,c,g,C,b){const O=Math.floor(r/i),x=Math.floor(c/i),T=Math.floor(g/i),S=Math.floor(C/i);for(let L=x;L<x+S;L++)for(let y=O;y<O+T;y++)u(y,L)&&(b.table[L][y]=1)}function m(r,c){if(!J(r,i)||!J(c,i))return!1;const g=Math.floor(r/i),C=Math.floor(c/i);return u(g,C)}for(const r of s){const[c,g,C,b]=K(r,o,n);if(!m(c,g))continue;let O=Q(h,r);O===-1&&(O=h.length,h.push(new U(r.ObjType,r.ObjSound,JSON.parse(JSON.stringify(f))))),p(c,g,C,b,h[O])}return h}class et{constructor(e,s,o,n,i,a){_(this,"x");_(this,"y");_(this,"width");_(this,"height");_(this,"type");_(this,"sound");this.x=e,this.y=s,this.width=o,this.height=n,this.type=i,this.sound=a}}function Y(t){return t===1}function v(t){const e=t.length,s=e>0?t[0].length:0;for(let o=0;o<s;o++)for(let n=0;n<e;n++)if(Y(t[n][o]))return[o,n];return[-1,-1]}function ot(t,e,s,o){for(let n=s;n<o;n++)if(!Y(t[e][n]))return!1;return!0}function nt(t,e){for(let s=t.y;s<t.height+t.y;s++)for(let o=t.x;o<t.width+t.x;o++)e[s][o]=0}function st(t){const e=t.type,s=t.sound,o=t.table.length,n=t.table[0].length,i=[],a=JSON.parse(JSON.stringify(t.table));function l(m,r,c,g){return new et(m,r,c,g,e,s)}let[f,h]=v(a),u=h,p=f+1;for(;f!==-1&&h!==-1;){let m=!0;for(;p<n&&m;){const x=a[u][p];m=Y(x),m&&p++}const r=p;u++;let c=!0;for(;u<o&&c;)c=ot(a,u,f,r),c&&u++;const g=u,C=r-f,b=g-h,O=l(f,h,C,b);i.push(O),nt(O,a),[f,h]=v(a),u=h,p=f+1}return i}function it(t,e,s){const o={};let n=!1;const i=(l,f)=>({X:(l.x*e).toString(),Y:(l.y*e).toString(),ObjWallWidth:(l.width*e).toString(),ObjWallHeight:(l.height*e).toString(),ID:f.toString(),ObjIndexID:"46",Name:"Wall Tool",LogidID:f.toString(),Poly:"0",ObjIsTile:"0",Depth:"500",ObjType:l.type,ObjSound:l.sound,Team:"-1"});s.forEach((l,f)=>{"Author"in l?o.Config=l:o[`OBJ${f}`]=l}),t.forEach((l,f)=>{const h=s.length+f;o[`OBJ${h}`]=i(l,h)});let a="";try{a=JSON.stringify(o)}catch{n=!0,console.error('Failed to serialize via "JSON.stringify"')}return n?[JSON.stringify(o),n]:[a,n]}const rt="#808080",lt="#00ff00",ct="#ffff00",at="#ffa040",ft="#ff0000",dt="#ff00ff",ht="#008080",ut="#000080",gt="#9f31c6",pt="#ff6200",D={0:rt,1:lt,2:ct,3:at,4:ft,5:dt,6:ht,7:ut,8:"#ffffff",9:gt,10:pt},F=32,E=B/F,d=20/F;function mt(t,e,s){console.clear();const o=t,n=JSON.parse(o[P]),[i,a]=k(n),[l,f]=q(n,Z),h=tt(i,a,l,$,A,E);e.width=i/E*d,e.height=a/E*d,s.width=e.width,s.height=e.height;const u=e.getContext("2d"),p=s.getContext("2d");l.forEach(T=>{const[S,L,y,M]=K(T,$,A),[N,w,R,j]=[Math.floor(S/E),Math.floor(L/E),Math.floor(y/E),Math.floor(M/E)];u.fillStyle="blue",(R===0||j===0)&&(console.log(`x: ${S}, y: ${L}, width: ${y}, height: ${M}, scaledX: ${N}, scaledY: ${w}, scaledWidth: ${R}, scaledHeight: ${j}`),u.fillStyle="red"),u.fillRect(N*d,w*d,R*d,j*d),u.fillStyle=D[T.ObjType],u.fillRect(N*d+2,w*d+2,R*d-4,j*d-4)});let m=[];h.forEach(T=>{const S=st(T);m=[...m,...S],S.forEach(L=>{const{x:y,y:M,width:N,height:w}=L;p.fillStyle="black",p.fillRect(y*d,M*d,d*N,d*w),p.fillStyle=D[T.type],p.fillRect(y*d+2,M*d+2,d*N-4,d*w-4)})});const r=l.length,c=m.length,g=Math.floor((1-c/r)*100);if(console.log(`Before: ${r}, After: ${c}`),console.log(`Compression ratio: ${g}%`),c>=r)return console.log("No optimization to be made"),[t,{before:r,after:r,ratio:0,hasCrashed:!1}];const[C,b]=it(m,E,f),O={before:r,after:c,ratio:g,hasCrashed:b};return[[...o.slice(0,P),C,o[P+1]],O]}const H=document.getElementById("progress"),X=document.getElementById("input_load_file"),Ot=document.getElementById("map_content"),yt=document.getElementById("before"),_t=document.getElementById("after"),Ct=document.getElementById("ratio"),Lt=document.getElementById("og_map_canvas"),I=document.getElementById("optimized_map_canvas");I.addEventListener("mouseenter",()=>I.className="disappear");I.addEventListener("mouseleave",()=>I.className="");let W=[];X.addEventListener("change",async()=>{var n;const t=(n=X.files)==null?void 0:n[0];if(W=[],!t)return;H.style.display="block";const e=await t.text();W.push(...e.split(`\r
`));const[s,o]=mt(W,Lt,I);if(o.has_crashed){alert("The optimization has crashed! This map is not suitable for optimization.");return}H.style.display="none",Ot.value=s.join(`
`),yt.textContent=o.before.toString(),_t.textContent=o.after.toString(),Ct.textContent=o.ratio.toString()});
