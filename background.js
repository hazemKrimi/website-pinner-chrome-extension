chrome.contextMenus.create({
    title: 'Pin',
    onclick: (page, tab) => {
        chrome.windows.create({
            url: page.pageUrl,
            width: 800,
            height: 600,
            incognito: tab.incognito,
            focused: true,
            type: 'popup'
        }, window => {
            chrome.tabs.onUpdated.addListener(async (id, changeInfo, tab) => {
                if (id === window.tabs[0].id && changeInfo.status === 'complete')
                    await fetch('http://localhost:8000/', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ title: tab.title })
                    });
            });
        });
    }
});