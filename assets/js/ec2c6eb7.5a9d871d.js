(window.webpackJsonp=window.webpackJsonp||[]).push([[42],{113:function(e,n,t){"use strict";t.r(n),t.d(n,"frontMatter",(function(){return i})),t.d(n,"metadata",(function(){return s})),t.d(n,"toc",(function(){return c})),t.d(n,"default",(function(){return l}));var r=t(3),o=t(7),a=(t(0),t(121)),i={sidebar_position:1},s={unversionedId:"buildsensornodes/sensors-and-comm",id:"buildsensornodes/sensors-and-comm",isDocsHomePage:!1,title:"Sensors and communication protocols",description:"Docusaurus can manage multiple versions of your docs.",source:"@site/docs/buildsensornodes/sensors-and-comm.md",sourceDirName:"buildsensornodes",slug:"/buildsensornodes/sensors-and-comm",permalink:"/IoT/docs/buildsensornodes/sensors-and-comm",editUrl:"https://github.com/OpenWaterNetwork/IoT/edit/main/website/docs/buildsensornodes/sensors-and-comm.md",version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Gateway registration on TTN",permalink:"/IoT/docs/buildloragateway/gatewayonttn"},next:{title:"Printed Circuit Boards (PCBs)",permalink:"/IoT/docs/buildsensornodes/pcbs"}},c=[{value:"Create a docs version",id:"create-a-docs-version",children:[]},{value:"Add a Version Dropdown",id:"add-a-version-dropdown",children:[]},{value:"Update an existing version",id:"update-an-existing-version",children:[]}],d={toc:c};function l(e){var n=e.components,i=Object(o.a)(e,["components"]);return Object(a.b)("wrapper",Object(r.a)({},d,i,{components:n,mdxType:"MDXLayout"}),Object(a.b)("p",null,"Docusaurus can manage multiple versions of your docs."),Object(a.b)("h2",{id:"create-a-docs-version"},"Create a docs version"),Object(a.b)("p",null,"Release a version 1.0 of your project:"),Object(a.b)("pre",null,Object(a.b)("code",{parentName:"pre",className:"language-bash"},"npm run docusaurus docs:version 1.0\n")),Object(a.b)("p",null,"The ",Object(a.b)("inlineCode",{parentName:"p"},"docs")," folder is copied into ",Object(a.b)("inlineCode",{parentName:"p"},"versioned_docs/version-1.0")," and ",Object(a.b)("inlineCode",{parentName:"p"},"versions.json")," is created."),Object(a.b)("p",null,"Your docs now have 2 versions:"),Object(a.b)("ul",null,Object(a.b)("li",{parentName:"ul"},Object(a.b)("inlineCode",{parentName:"li"},"1.0")," at ",Object(a.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/")," for the version 1.0 docs"),Object(a.b)("li",{parentName:"ul"},Object(a.b)("inlineCode",{parentName:"li"},"current")," at ",Object(a.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/next/")," for the ",Object(a.b)("strong",{parentName:"li"},"upcoming, unreleased docs"))),Object(a.b)("h2",{id:"add-a-version-dropdown"},"Add a Version Dropdown"),Object(a.b)("p",null,"To navigate seamlessly across versions, add a version dropdown."),Object(a.b)("p",null,"Modify the ",Object(a.b)("inlineCode",{parentName:"p"},"docusaurus.config.js")," file:"),Object(a.b)("pre",null,Object(a.b)("code",{parentName:"pre",className:"language-js",metastring:'title="docusaurus.config.js"',title:'"docusaurus.config.js"'},"module.exports = {\n  themeConfig: {\n    navbar: {\n      items: [\n        // highlight-start\n        {\n          type: 'docsVersionDropdown',\n        },\n        // highlight-end\n      ],\n    },\n  },\n};\n")),Object(a.b)("p",null,"The docs version dropdown appears in your navbar:"),Object(a.b)("p",null,Object(a.b)("img",{alt:"Docs Version Dropdown",src:t(129).default})),Object(a.b)("h2",{id:"update-an-existing-version"},"Update an existing version"),Object(a.b)("p",null,"It is possible to edit versioned docs in their respective folder:"),Object(a.b)("ul",null,Object(a.b)("li",{parentName:"ul"},Object(a.b)("inlineCode",{parentName:"li"},"versioned_docs/version-1.0/hello.md")," updates ",Object(a.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/hello")),Object(a.b)("li",{parentName:"ul"},Object(a.b)("inlineCode",{parentName:"li"},"docs/hello.md")," updates ",Object(a.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/next/hello"))))}l.isMDXComponent=!0},121:function(e,n,t){"use strict";t.d(n,"a",(function(){return u})),t.d(n,"b",(function(){return m}));var r=t(0),o=t.n(r);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function s(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function c(e,n){if(null==e)return{};var t,r,o=function(e,n){if(null==e)return{};var t,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(o[t]=e[t]);return o}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var d=o.a.createContext({}),l=function(e){var n=o.a.useContext(d),t=n;return e&&(t="function"==typeof e?e(n):s(s({},n),e)),t},u=function(e){var n=l(e.components);return o.a.createElement(d.Provider,{value:n},e.children)},p={inlineCode:"code",wrapper:function(e){var n=e.children;return o.a.createElement(o.a.Fragment,{},n)}},b=o.a.forwardRef((function(e,n){var t=e.components,r=e.mdxType,a=e.originalType,i=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),u=l(t),b=r,m=u["".concat(i,".").concat(b)]||u[b]||p[b]||a;return t?o.a.createElement(m,s(s({ref:n},d),{},{components:t})):o.a.createElement(m,s({ref:n},d))}));function m(e,n){var t=arguments,r=n&&n.mdxType;if("string"==typeof e||r){var a=t.length,i=new Array(a);i[0]=b;var s={};for(var c in n)hasOwnProperty.call(n,c)&&(s[c]=n[c]);s.originalType=e,s.mdxType="string"==typeof e?e:r,i[1]=s;for(var d=2;d<a;d++)i[d]=t[d];return o.a.createElement.apply(null,i)}return o.a.createElement.apply(null,t)}b.displayName="MDXCreateElement"},129:function(e,n,t){"use strict";t.r(n),n.default=t.p+"assets/images/docsVersionDropdown-dda80f009a926fb2dd92bab8faa6c4d8.png"}}]);