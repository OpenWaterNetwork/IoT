(window.webpackJsonp=window.webpackJsonp||[]).push([[34],{105:function(e,n,t){"use strict";t.r(n),t.d(n,"frontMatter",(function(){return i})),t.d(n,"metadata",(function(){return c})),t.d(n,"toc",(function(){return s})),t.d(n,"default",(function(){return d}));var r=t(3),a=t(7),o=(t(0),t(121)),i={sidebar_position:3},c={unversionedId:"buildsensornodes/sensornodesttn",id:"buildsensornodes/sensornodesttn",isDocsHomePage:!1,title:"Water sensor expansion board 1.0 for LoPy4/FiPy/GPy/SiPy/WiPy",description:"Let's translate docs/getting-started.md to French.",source:"@site/docs/buildsensornodes/sensornodesttn.md",sourceDirName:"buildsensornodes",slug:"/buildsensornodes/sensornodesttn",permalink:"/IoT/docs/buildsensornodes/sensornodesttn",editUrl:"https://github.com/OpenWaterNetwork/IoT/edit/main/website/docs/buildsensornodes/sensornodesttn.md",version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Printed Circuit Boards (PCBs)",permalink:"/IoT/docs/buildsensornodes/pcbs"},next:{title:"Sensor node registration on TTN",permalink:"/IoT/docs/buildsensornodes/wseb"}},s=[{value:"Configure i18n",id:"configure-i18n",children:[]},{value:"Translate a doc",id:"translate-a-doc",children:[]},{value:"Start your localized site",id:"start-your-localized-site",children:[]},{value:"Add a Locale Dropdown",id:"add-a-locale-dropdown",children:[]},{value:"Build your localized site",id:"build-your-localized-site",children:[]}],l={toc:s};function d(e){var n=e.components,i=Object(a.a)(e,["components"]);return Object(o.b)("wrapper",Object(r.a)({},l,i,{components:n,mdxType:"MDXLayout"}),Object(o.b)("p",null,"Let's translate ",Object(o.b)("inlineCode",{parentName:"p"},"docs/getting-started.md")," to French."),Object(o.b)("h2",{id:"configure-i18n"},"Configure i18n"),Object(o.b)("p",null,"Modify ",Object(o.b)("inlineCode",{parentName:"p"},"docusaurus.config.js")," to add support for the ",Object(o.b)("inlineCode",{parentName:"p"},"fr")," locale:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-js",metastring:'title="docusaurus.config.js"',title:'"docusaurus.config.js"'},"module.exports = {\n  i18n: {\n    defaultLocale: 'en',\n    locales: ['en', 'fr'],\n  },\n};\n")),Object(o.b)("h2",{id:"translate-a-doc"},"Translate a doc"),Object(o.b)("p",null,"Copy the ",Object(o.b)("inlineCode",{parentName:"p"},"docs/getting-started.md")," file to the ",Object(o.b)("inlineCode",{parentName:"p"},"i18n/fr")," folder:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"mkdir -p i18n/fr/docusaurus-plugin-content-docs/current/\n\ncp docs/getting-started.md i18n/fr/docusaurus-plugin-content-docs/current/getting-started.md\n")),Object(o.b)("p",null,"Translate ",Object(o.b)("inlineCode",{parentName:"p"},"i18n/fr/docusaurus-plugin-content-docs/current/getting-started.md")," in French."),Object(o.b)("h2",{id:"start-your-localized-site"},"Start your localized site"),Object(o.b)("p",null,"Start your site on the French locale:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"npm run start -- --locale fr\n")),Object(o.b)("p",null,"Your localized site is accessible at ",Object(o.b)("inlineCode",{parentName:"p"},"http://localhost:3000/fr/")," and the ",Object(o.b)("inlineCode",{parentName:"p"},"Getting Started")," page is translated."),Object(o.b)("div",{className:"admonition admonition-caution alert alert--warning"},Object(o.b)("div",{parentName:"div",className:"admonition-heading"},Object(o.b)("h5",{parentName:"div"},Object(o.b)("span",{parentName:"h5",className:"admonition-icon"},Object(o.b)("svg",{parentName:"span",xmlns:"http://www.w3.org/2000/svg",width:"16",height:"16",viewBox:"0 0 16 16"},Object(o.b)("path",{parentName:"svg",fillRule:"evenodd",d:"M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"}))),"caution")),Object(o.b)("div",{parentName:"div",className:"admonition-content"},Object(o.b)("p",{parentName:"div"},"In development, you can only use one locale at a same time."))),Object(o.b)("h2",{id:"add-a-locale-dropdown"},"Add a Locale Dropdown"),Object(o.b)("p",null,"To navigate seamlessly across languages, add a locale dropdown."),Object(o.b)("p",null,"Modify the ",Object(o.b)("inlineCode",{parentName:"p"},"docusaurus.config.js")," file:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-js",metastring:'title="docusaurus.config.js"',title:'"docusaurus.config.js"'},"module.exports = {\n  themeConfig: {\n    navbar: {\n      items: [\n        // highlight-start\n        {\n          type: 'localeDropdown',\n        },\n        // highlight-end\n      ],\n    },\n  },\n};\n")),Object(o.b)("p",null,"The locale dropdown now appears in your navbar:"),Object(o.b)("p",null,Object(o.b)("img",{alt:"Locale Dropdown",src:t(126).default})),Object(o.b)("h2",{id:"build-your-localized-site"},"Build your localized site"),Object(o.b)("p",null,"Build your site for a specific locale:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"npm run build -- --locale fr\n")),Object(o.b)("p",null,"Or build your site to include all the locales at once:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"npm run build\n")))}d.isMDXComponent=!0},121:function(e,n,t){"use strict";t.d(n,"a",(function(){return u})),t.d(n,"b",(function(){return m}));var r=t(0),a=t.n(r);function o(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function c(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){o(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var l=a.a.createContext({}),d=function(e){var n=a.a.useContext(l),t=n;return e&&(t="function"==typeof e?e(n):c(c({},n),e)),t},u=function(e){var n=d(e.components);return a.a.createElement(l.Provider,{value:n},e.children)},p={inlineCode:"code",wrapper:function(e){var n=e.children;return a.a.createElement(a.a.Fragment,{},n)}},b=a.a.forwardRef((function(e,n){var t=e.components,r=e.mdxType,o=e.originalType,i=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),u=d(t),b=r,m=u["".concat(i,".").concat(b)]||u[b]||p[b]||o;return t?a.a.createElement(m,c(c({ref:n},l),{},{components:t})):a.a.createElement(m,c({ref:n},l))}));function m(e,n){var t=arguments,r=n&&n.mdxType;if("string"==typeof e||r){var o=t.length,i=new Array(o);i[0]=b;var c={};for(var s in n)hasOwnProperty.call(n,s)&&(c[s]=n[s]);c.originalType=e,c.mdxType="string"==typeof e?e:r,i[1]=c;for(var l=2;l<o;l++)i[l]=t[l];return a.a.createElement.apply(null,i)}return a.a.createElement.apply(null,t)}b.displayName="MDXCreateElement"},126:function(e,n,t){"use strict";t.r(n),n.default=t.p+"assets/images/localeDropdown-0052c3f08ccaf802ac733b23e655f498.png"}}]);