/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'OpenWaterNetwork',
  tagline: 'Promoting Open Source and Open Access data for Water Resource Management',
  url: 'https://fabianastudillo.github.io',
  baseUrl: '/IoT/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'OpenWaterNetwork', // Usually your GitHub org/user name.
  projectName: 'IoT', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'OpenWaterNetwork',
      logo: {
        alt: 'OpenWaterNetwork',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Tutorial',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Tutorial',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Twitter',
              href: 'https://twitter.com/openwaternetwork',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/OpenWaterNetwork/IoT',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Open Water Network.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/OpenWaterNetwork/IoT/edit/master/website/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/OpenWaterNetwork/IoT/edit/master/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
