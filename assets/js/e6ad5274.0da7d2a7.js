(window.webpackJsonp=window.webpackJsonp||[]).push([[39],{110:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return i})),n.d(t,"metadata",(function(){return l})),n.d(t,"toc",(function(){return c})),n.d(t,"default",(function(){return s}));var a=n(3),r=n(7),o=(n(0),n(121)),i={sidebar_position:2},l={unversionedId:"buildloragateway/pygate",id:"buildloragateway/pygate",isDocsHomePage:!1,title:"PyGate",description:"Let's translate docs/getting-started.md to French.",source:"@site/docs/buildloragateway/pygate.md",sourceDirName:"buildloragateway",slug:"/buildloragateway/pygate",permalink:"/IoT/docs/buildloragateway/pygate",editUrl:"https://github.com/OpenWaterNetwork/IoT/edit/main/website/docs/buildloragateway/pygate.md",version:"current",sidebarPosition:2,frontMatter:{sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"Gateway",permalink:"/IoT/docs/buildloragateway/gateway"},next:{title:"Gateway registration on TTN",permalink:"/IoT/docs/buildloragateway/gatewayonttn"}},c=[{value:"Configure i18n",id:"configure-i18n",children:[]},{value:"Translate a doc",id:"translate-a-doc",children:[]},{value:"Start your localized site",id:"start-your-localized-site",children:[]},{value:"Add a Locale Dropdown",id:"add-a-locale-dropdown",children:[]},{value:"Build your localized site",id:"build-your-localized-site",children:[]}],d={toc:c};function s(e){var t=e.components,i=Object(r.a)(e,["components"]);return Object(o.b)("wrapper",Object(a.a)({},d,i,{components:t,mdxType:"MDXLayout"}),Object(o.b)("p",null,"Let's translate ",Object(o.b)("inlineCode",{parentName:"p"},"docs/getting-started.md")," to French."),Object(o.b)("h2",{id:"configure-i18n"},"Configure i18n"),Object(o.b)("p",null,"Modify ",Object(o.b)("inlineCode",{parentName:"p"},"docusaurus.config.js")," to add support for the ",Object(o.b)("inlineCode",{parentName:"p"},"fr")," locale:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-js",metastring:'title="docusaurus.config.js"',title:'"docusaurus.config.js"'},"module.exports = {\n  i18n: {\n    defaultLocale: 'en',\n    locales: ['en', 'fr'],\n  },\n};\n")),Object(o.b)("h2",{id:"translate-a-doc"},"Translate a doc"),Object(o.b)("p",null,"Copy the ",Object(o.b)("inlineCode",{parentName:"p"},"docs/getting-started.md")," file to the ",Object(o.b)("inlineCode",{parentName:"p"},"i18n/fr")," folder:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"mkdir -p i18n/fr/docusaurus-plugin-content-docs/current/\n\ncp docs/getting-started.md i18n/fr/docusaurus-plugin-content-docs/current/getting-started.md\n")),Object(o.b)("p",null,"Translate ",Object(o.b)("inlineCode",{parentName:"p"},"i18n/fr/docusaurus-plugin-content-docs/current/getting-started.md")," in French."),Object(o.b)("h2",{id:"start-your-localized-site"},"Start your localized site"),Object(o.b)("p",null,"Start your site on the French locale:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"npm run start -- --locale fr\n")),Object(o.b)("p",null,"Your localized site is accessible at ",Object(o.b)("inlineCode",{parentName:"p"},"http://localhost:3000/fr/")," and the ",Object(o.b)("inlineCode",{parentName:"p"},"Getting Started")," page is translated."),Object(o.b)("div",{className:"admonition admonition-caution alert alert--warning"},Object(o.b)("div",{parentName:"div",className:"admonition-heading"},Object(o.b)("h5",{parentName:"div"},Object(o.b)("span",{parentName:"h5",className:"admonition-icon"},Object(o.b)("svg",{parentName:"span",xmlns:"http://www.w3.org/2000/svg",width:"16",height:"16",viewBox:"0 0 16 16"},Object(o.b)("path",{parentName:"svg",fillRule:"evenodd",d:"M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"}))),"caution")),Object(o.b)("div",{parentName:"div",className:"admonition-content"},Object(o.b)("p",{parentName:"div"},"In development, you can only use one locale at a same time."))),Object(o.b)("h2",{id:"add-a-locale-dropdown"},"Add a Locale Dropdown"),Object(o.b)("p",null,"To navigate seamlessly across languages, add a locale dropdown."),Object(o.b)("p",null,"Modify the ",Object(o.b)("inlineCode",{parentName:"p"},"docusaurus.config.js")," file:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-js",metastring:'title="docusaurus.config.js"',title:'"docusaurus.config.js"'},"module.exports = {\n  themeConfig: {\n    navbar: {\n      items: [\n        // highlight-start\n        {\n          type: 'localeDropdown',\n        },\n        // highlight-end\n      ],\n    },\n  },\n};\n")),Object(o.b)("p",null,"The locale dropdown now appears in your navbar:"),Object(o.b)("p",null,Object(o.b)("img",{alt:"Locale Dropdown",src:n(126).default})),Object(o.b)("h2",{id:"build-your-localized-site"},"Build your localized site"),Object(o.b)("p",null,"Build your site for a specific locale:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"npm run build -- --locale fr\n")),Object(o.b)("p",null,"Or build your site to include all the locales at once:"),Object(o.b)("pre",null,Object(o.b)("code",{parentName:"pre",className:"language-bash"},"npm run build\n")))}s.isMDXComponent=!0},121:function(e,t,n){"use strict";n.d(t,"a",(function(){return u})),n.d(t,"b",(function(){return m}));var a=n(0),r=n.n(a);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var d=r.a.createContext({}),s=function(e){var t=r.a.useContext(d),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},u=function(e){var t=s(e.components);return r.a.createElement(d.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.a.createElement(r.a.Fragment,{},t)}},b=r.a.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,i=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),u=s(n),b=a,m=u["".concat(i,".").concat(b)]||u[b]||p[b]||o;return n?r.a.createElement(m,l(l({ref:t},d),{},{components:n})):r.a.createElement(m,l({ref:t},d))}));function m(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=b;var l={};for(var c in t)hasOwnProperty.call(t,c)&&(l[c]=t[c]);l.originalType=e,l.mdxType="string"==typeof e?e:a,i[1]=l;for(var d=2;d<o;d++)i[d]=n[d];return r.a.createElement.apply(null,i)}return r.a.createElement.apply(null,n)}b.displayName="MDXCreateElement"},126:function(e,t,n){"use strict";n.r(t),t.default=n.p+"assets/images/localeDropdown-0052c3f08ccaf802ac733b23e655f498.png"}}]);