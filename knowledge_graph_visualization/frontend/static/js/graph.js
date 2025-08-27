// ȫ�ֱ���
let graphData = { nodes: [], links: [] }; // ͼ������
let svg, simulation; // D3 SVG������������ģ��

// ��ʼ��ͼ��
function initGraph() {
    const container = document.getElementById('graph-container');
    const width = container.clientWidth;
    const height = container.clientHeight;

    // ����SVG����
    svg = d3.select('#graph-container')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    // ������Ź���
    svg.call(d3.zoom().on('zoom', (event) => {
        g.attr('transform', event.transform);
    }));

    const g = svg.append('g');

    // ��ʼ�������򲼾�
    simulation = d3.forceSimulation()
        .force('link', d3.forceLink().id(d => d.id).distance(100))
        .force('charge', d3.forceManyBody().strength(-300))
        .force('center', d3.forceCenter(width / 2, height / 2));

    // �Ӻ�˼�������
    loadGraphData();
}

// �Ӻ��API����ͼ������
function loadGraphData() {
    fetch('/api/kg/data')
        .then(response => response.json())
        .then(res => {
            if (res.ret === 0) {
                graphData = res.data;
                updateGraph(); // ����ͼ����Ⱦ
            } else {
                console.error('��������ʧ��:', res.msg);
            }
        })
        .catch(error => console.error('����ʧ��:', error));
}

// ����ͼ����Ⱦ
function updateGraph() {
    // �������Ԫ��
    svg.selectAll('*').remove();

    // ���´���ͼ��
    const g = svg.append('g');

    // ���ƹ�ϵ��
    const link = g.append('g')
        .selectAll('line')
        .data(graphData.links)
        .enter().append('line')
        .attr('class', 'link')
        .attr('stroke-width', 2);

    // ����ʵ��ڵ�
    const node = g.append('g')
        .selectAll('g')
        .data(graphData.nodes)
        .enter().append('g')
        .attr('class', 'node')
        .call(d3.drag()
            .on('start', dragstarted)
            .on('drag', dragged)
            .on('end', dragended));

    // �ڵ����Բ��
    node.append('circle')
        .attr('r', 15)
        .attr('fill', d => {
            // ����ʵ������������ɫ
            const colors = { '����': '#4285f4', '��֯': '#34a853', '�ص�': '#fbbc05' };
            return colors[d.type] || '#ea4335';
        });

    // �ڵ��������
    node.append('text')
        .attr('dx', 20)
        .attr('dy', '.3em')
        .text(d => d.name);

    // ����������ģ��
    simulation.nodes(graphData.nodes)
        .on('tick', ticked);

    simulation.force('link')
        .links(graphData.links);

    simulation.alpha(1).restart();

    // �����򲼾ָ��»ص�
    function ticked() {
        link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y);

        node.attr('transform', d => `translate(${d.x},${d.y})`);
    }
}

// ��ק�¼�����
function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
}

function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

// ���ļ����뵼���¼�
function bindEvents() {
    // ����JSON�ļ�
    document.getElementById('import-btn').addEventListener('click', () => {
        document.getElementById('file-upload').click();
    });

    document.getElementById('file-upload').addEventListener('change', handleFileImport);

    // ������ǰ����
    document.getElementById('export-btn').addEventListener('click', exportGraphData);

    // ����ʵ��
    document.getElementById('add-entity-btn').addEventListener('click', addNewEntity);
}

// �����ļ�����
function handleFileImport(event) {
    const file = event.target.files[0];
    if (!file || !file.name.endsWith('.json')) {
        alert('��ѡ��JSON�ļ�');
        return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
        try {
            const data = JSON.parse(e.target.result);
            if (data.nodes && data.links) {
                graphData = data;
                updateGraph();
                alert('����ɹ�');
            } else {
                alert('JSON��ʽ���������nodes��links');
            }
        } catch (error) {
            alert('����ʧ��: ' + error.message);
        }
    };
    reader.readAsText(file);
}

// ������ǰ����
function exportGraphData() {
    const dataStr = JSON.stringify(graphData, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `knowledge_graph_${new Date().getTime()}.json`;
    a.click();
    URL.revokeObjectURL(url);
}

// ����ʵ�嵽���
function addNewEntity() {
    const id = document.getElementById('entity-id').value;
    const name = document.getElementById('entity-name').value;
    if (!id || !name) {
        alert('������ʵ��ID������');
        return;
    }

    fetch('/api/kg/entity', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id, name })
    })
    .then(response => response.json())
    .then(res => {
        if (res.ret === 0) {
            alert('ʵ����ӳɹ�');
            loadGraphData(); // ���¼�������
        } else {
            alert('���ʧ��: ' + res.msg);
        }
    });
}

// ҳ�������ɺ��ʼ��
window.onload = () => {
    initGraph();
    bindEvents();
};