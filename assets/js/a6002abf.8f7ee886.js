(window.webpackJsonp=window.webpackJsonp||[]).push([[28],{100:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return i})),n.d(t,"metadata",(function(){return c})),n.d(t,"toc",(function(){return l})),n.d(t,"default",(function(){return s}));var a=n(3),r=n(7),o=(n(0),n(121)),i={sidebar_position:8},c={unversionedId:"handsontraining/module8",id:"handsontraining/module8",isDocsHomePage:!1,title:"Module 8 - Building your own LoRa Gateway for data transmission",description:"Add Markdown or React files to src/pages to create a standalone page:",source:"@site/docs/handsontraining/module8.md",sourceDirName:"handsontraining",slug:"/handsontraining/module8",permalink:"/IoT/docs/handsontraining/module8",editUrl:"https://github.com/OpenWaterNetwork/IoT/tree/documentation/docs/handsontraining/module8.md",version:"current",sidebarPosition:8,frontMatter:{sidebar_position:8},sidebar:"tutorialSidebar",previous:{title:"Module 7 - Keeping time and introducing the deep sleep concept",permalink:"/IoT/docs/handsontraining/module7"},next:{title:"Module 9 - IoT Data transmission, storage,  visualization and download",permalink:"/IoT/docs/handsontraining/module9"}},l=[{value:"Create your first React Page",id:"create-your-first-react-page",children:[]},{value:"Create your first Markdown Page",id:"create-your-first-markdown-page",children:[]}],p={toc:l};function s(e){var t=e.components,n=Object(r.a)(e,["components"]);return Object(o.b)("wrapper",Object(a.a)({},p,n,{components:t,mdxType:"MDXLayout"}),Object(o.b)("p",null,"Add ",Object(o.b)("strong",{parentName:"p"},"Markdown or React")," files to ",Object(o.b)("inlineCode",{parentName:"p"},"src/pages")," to create a ",Object(o.b)("strong",{parentName:"p"},"standalone page"),":"),Object(o.b)("ul",null,Object(o.b)("li",{parentName:"ul"},Object(o.b)("inlineCode",{parentName:"li"},"src/pages/index.js")," -> ",Object(o.b)("inlineCode",{parentName:"li"},"localhost:3000/")),Object(o.b)("li",{parentName:"ul"},Object(o.b)("inlineCode",{parentName:"li"},"src/pages/foo.md")," -> ",Object(o.b)("inlineCode",{parentName:"li"},"localhost:3000/foo")),Object(o.b)("li",{parentName:"ul"},Object(o.b)("inlineCode",{parentName:"li"},"src/pages/foo/bar.js")," -> ",Object(o.b)("inlineCode",{parentName:"li"},"localhost:3000/foo/bar"))),Object(o.b)("h2",{id:"create-your-first-react-page"},"Create your first React Page"),Object(o.b)("p",null,"Create a file at ",Object(o.b)("inlineCode",{parentName:"p"},"src/pages/my-react-page.js"),":"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-jsx",metastring:'title="src/pages/my-react-page.js"',title:'"src/pages/my-react-page.js"'},"import React from 'react';\nimport Layout from '@theme/Layout';\n\nexport default function MyReactPage() {\n  return (\n    <Layout>\n      <h1>My React page</h1>\n      <p>This is a React page</p>\n    </Layout>\n  );\n}\n")),Object(o.b)("p",null,"A new page is now available at ",Object(o.b)("inlineCode",{parentName:"p"},"http://localhost:3000/my-react-page"),"."),Object(o.b)("h2",{id:"create-your-first-markdown-page"},"Create your first Markdown Page"),Object(o.b)("p",null,"Create a file at ",Object(o.b)("inlineCode",{parentName:"p"},"src/pages/my-markdown-page.md"),":"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-mdx",metastring:'title="src/pages/my-markdown-page.md"',title:'"src/pages/my-markdown-page.md"'},"# My Markdown page\n\nThis is a Markdown page\n")),Object(o.b)("p",null,"A new page is now available at ",Object(o.b)("inlineCode",{parentName:"p"},"http://localhost:3000/my-markdown-page"),"."))}s.isMDXComponent=!0},121:function(e,t,n){"use strict";n.d(t,"a",(function(){return d})),n.d(t,"b",(function(){return m}));var a=n(0),r=n.n(a);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function c(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var p=r.a.createContext({}),s=function(e){var t=r.a.useContext(p),n=t;return e&&(n="function"==typeof e?e(t):c(c({},t),e)),n},d=function(e){var t=s(e.components);return r.a.createElement(p.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.a.createElement(r.a.Fragment,{},t)}},b=r.a.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,i=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),d=s(n),b=a,m=d["".concat(i,".").concat(b)]||d[b]||u[b]||o;return n?r.a.createElement(m,c(c({ref:t},p),{},{components:n})):r.a.createElement(m,c({ref:t},p))}));function m(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=b;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c.mdxType="string"==typeof e?e:a,i[1]=c;for(var p=2;p<o;p++)i[p]=n[p];return r.a.createElement.apply(null,i)}return r.a.createElement.apply(null,n)}b.displayName="MDXCreateElement"}}]);